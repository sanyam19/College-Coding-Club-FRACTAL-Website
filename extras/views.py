
from django.shortcuts import render, get_object_or_404
from fractalweb.models import ExtendedUser
from .models import Questions,Tag,Category,resourses
from classroom.models import Question,Archive
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse ,HttpResponseRedirect

def question(request):
	if request.method == 'POST':
		quote = request.POST.get('language')
		quote1 = request.POST.get('status')
		# print(quote,quote1,"sda")
		return HttpResponseRedirect('/extra/filter/?tag='+quote+'&category='+str(quote1))
	questions_list=Questions.objects.all().order_by('-question_date')
	tag_list=Tag.objects.all()
	cat_list=Category.objects.all()
	page = request.GET.get('page', 1)

	paginator = Paginator(questions_list, 10)
	try:
		questions = paginator.page(page)
	except PageNotAnInteger:
		questions = paginator.page(1)
	except EmptyPage:
		questions = paginator.page(paginator.num_pages)

	return render(request, 'extras/questions.html', {'questions': questions,'tags':tag_list,'category':cat_list})

def filter(request):
	tagvalue = quote = request.GET.get('tag')
	categoryvalue = quote1 = request.GET.get('category')
	# print(tagvalue,categoryvalue,"asasasas")
	if not(quote or quote1):
		p=Questions.objects.all()
		page = request.GET.get('page', 1)
		paginator = Paginator(p, 10)
		try:
			questions = paginator.page(page)
		except PageNotAnInteger:
			questions = paginator.page(1)
		except EmptyPage:
			questions = paginator.page(paginator.num_pages)
		context ={ 
		'filterap':questions,
		'filters':questions,
		}		

	elif not quote:
		quote1=list(Category.objects.filter(category_name=quote1))[0]
		p=list(Questions.objects.filter(category=quote1))
		page = request.GET.get('page', 1)
		paginator = Paginator(p, 10)
		try:
			questions = paginator.page(page)
		except PageNotAnInteger:
			questions = paginator.page(1)
		except EmptyPage:
			questions = paginator.page(paginator.num_pages)
		context ={ 
		'filterap':questions,
		'filters':questions,
		}
	
	elif not quote1:
		quote=list(Tag.objects.filter(pk=int(quote)))[0]
		p=list(Questions.objects.filter(tags=quote))
		page = request.GET.get('page', 1)
		paginator = Paginator(p, 10)
		try:
			questions = paginator.page(page)
		except PageNotAnInteger:
			questions = paginator.page(1)
		except EmptyPage:
			questions = paginator.page(paginator.num_pages)
		context ={ 
		'filterap':questions,
		'filters':questions,
		}
	
	elif quote and quote1:
		quote=list(Tag.objects.filter(pk=int(quote)))[0]
		quote1=list(Category.objects.filter(category_name=quote1))[0]
		p=list(Questions.objects.filter(tags=quote,category=quote1))
		page = request.GET.get('page', 1)
		paginator = Paginator(p, 10)
		try:
			questions = paginator.page(page)
		except PageNotAnInteger:
			questions = paginator.page(1)
		except EmptyPage:
			questions = paginator.page(paginator.num_pages)
		context ={ 
		'filterap':questions,
		'filters':questions,
		}
	context['tagvalue']=str(tagvalue)
	context['categoryvalue']=str(categoryvalue)
	return render(request,'extras/filter.html',context=context) 		

def explore(request):
    return render(request, 'extras/explore.html', {})

def resources(request):
	resources_list=resourses.objects.all().order_by('-date')
	page = request.GET.get('page', 1)

	paginator = Paginator(resources_list, 10)
	try:
		resources = paginator.page(page)
	except PageNotAnInteger:
		resources = paginator.page(1)
	except EmptyPage:
		resources = paginator.page(paginator.num_pages)

	return render(request, 'extras/resources.html', {'resources': resources})

	
# Create your views here.