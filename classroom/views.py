from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Question,Slide,Archive,Schedule
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from fractalweb.models import ExtendedUser
@login_required
def classroom(request):
    return render(request, 'classroom/classroom.html', {})

@login_required
def question(request):
	# print(request.user)
	quote=ExtendedUser.objects.get(user=request.user).sessions
	print(quote,"\n\n\n\n\n")
	# for u in ulist:
	# 	if u.user==request.user:
	# 		quote=u.sessions
	# 		break

	if quote:
		
		p=Question.objects.filter(session__session=quote)
		
		context ={ 
			'filterap':p#,pp],
			#'filterapp':pp,
			}
		#return render(request,'classroom/ques_filter.html',context=context) 

	else:
		notfound="Enter Tags Or Category to filter"	
		return render(request,'classroom/questions.html', {'notfound':notfound})

	questionns_list=p.order_by('-question_date')
	q1=p.count()
	page = request.GET.get('page', 1)
	paginator = Paginator(questionns_list, 10)
	try:
		questionns= paginator.page(page)
	except PageNotAnInteger:
		questionns = paginator.page(1)
	except EmptyPage:
		questionns= paginator.page(paginator.num_pages)
	return render(request, 'classroom/questions.html', {'questionns': questionns,'q1':q1,'session':quote})
    #return render(request, 'classroom/question.html', {})

@login_required
def slide(request):
	quote=ExtendedUser.objects.get(user=request.user).sessions
	#print(quote,"\n\n\n\n\n")
	# for u in ulist:
	# 	if u.user==request.user:
	# 		quote=u.sessions
	# 		break

	if quote:
		
		p=Slide.objects.filter(session__session=quote)
		
		context ={ 
			'filterap':p#,pp],
			#'filterapp':pp,
			}
		#return render(request,'classroom/ques_filter.html',context=context) 

	else:
		notfound="Enter Tags Or Category to filter"	
		return render(request,'classroom/slide.html', {'notfound':notfound})

	slide_list=p.order_by('-question_date')

	page = request.GET.get('page', 1)
	paginator = Paginator(slide_list, 10)
	try:
		slide = paginator.page(page)
	except PageNotAnInteger:
		slide = paginator.page(1)
	except EmptyPage:
		slide = paginator.page(paginator.num_pages)
	return render(request, 'classroom/slide.html', {'slide': slide,'session':quote})

@login_required
def archive(request):

	if request.method == 'POST':	
		import requests
		u=ExtendedUser.objects.get(user=request.user)
		u.sessions=request.POST['quote']
		u.save()
	archive=Archive.objects.all().order_by('-id')
	# page = request.GET.get('page', 1)
	# paginator = Paginator(archive_list, 20)
	# try:
	# 	archive = paginator.page(page)
	# except PageNotAnInteger:
	# 	archive= paginator.page(1)
	# except EmptyPage:
	# 	archive= paginator.page(paginator.num_pages)
	return render(request, 'classroom/archive.html', {'archive': archive})

@login_required
def schedule(request):
	schedule_list=Schedule.objects.all().order_by('-schedule_date')
	page = request.GET.get('page', 1)
	paginator = Paginator(schedule_list, 10)
	try:
		schedule= paginator.page(page)
	except PageNotAnInteger:
		schedule = paginator.page(1)
	except EmptyPage:
		schedule= paginator.page(paginator.num_pages)
	return render(request, 'classroom/schedule.html', {'schedule': schedule})
# Create your views here.
#@login_required
#def ques_filter(request):
	