from django.shortcuts import render, get_object_or_404, redirect
from .models import ExtendedUser
from extras.models import Questions,Tag,Category
from classroom.models import Question,Archive
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from classroom import views
from extras import views
from . import views
from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from .forms import UpdateExcelForm
from .models import UploadForm,Upload
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.models import User
from .models import ExtendedUser
from django.contrib.auth import authenticate,login,logout
import classroom.views  
def error_404_view(request, exception):
    return render(request,'fractalweb/error_404.html',{})

def home(request):
	return render(request, 'fractalweb/index.html', {})

def announcements(request):
    return render(request,'fractalweb/announcements.html',{})

def about(request):
    return render(request,'fractalweb/about.html',{})    


def register(request):
    message=""
    if request.method == 'POST':
        import requests
        token = request.POST['token']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        extendUser = ExtendedUser.objects.filter(token=token)
        if extendUser:
            extendUser=list(extendUser)[0]
            if extendUser.user.is_active:
                message="Enter information correctly!!"
                return render(request,'register.html', {'message':message}) 

            else:
                if password1 == password2:
                    extendUser.user.set_password(password1)
                    extendUser.user.is_active=True
                    extendUser.user.is_valid=True
                    extendUser.token=None
                    context={
                    'fname':extendUser.user.first_name,
                    'lname':extendUser.user.last_name,
                    'uname':extendUser.user.username,
                    'email':extendUser.user.email,
                    'rollnum':extendUser.rollno,
                    'phonenum':extendUser.phone,
                    'branch':extendUser.branch,
                    'session':extendUser.sessions,
                    'flag':True,
                    }
                    extendUser.save()
                    extendUser.user.save()
                    return render(request,'register.html',context=context)
                else:
                    message="Enter information correctly!!"
                    return render(request,'register.html', {'message':message})   

        else:
            message="Enter information correctly!!"
            return render(request,'register.html', {'message':message})


    else:
        return render(request,'register.html', {'message':message})
            

def LogInView(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                # return render(request,'classroom/questions.html')
                # return redirect(classroom.views.question)
                return HttpResponseRedirect('/classroom/question/')
            else:
                content_dic={'error':'You are a Inactive User Contact Admin'}
                return render(request,'registration/login.html',context=content_dic)
        else:
            content_dic={'error':'Invalid Roll Number or Password'}
            return render(request,'registration/login.html',context=content_dic)
    else:
        return render(request,'registration/login.html')




@login_required
def update_excel(request):
    if request.user.is_superuser:
        message=''
        if request.method == 'POST':
            form = UpdateExcelForm(request.POST, request.FILES)
            if form.is_valid():
                from fractalweb.models import ExtendedUser
                excel_file = request.FILES['excel_file']
            import os
            import tempfile
            import xlrd
            fd, path = tempfile.mkstemp() #  mkstemp returns a tuple: an integer (index) called file descriptor used by OS to refer to a file and its path
            try:
                with os.fdopen(fd, 'wb') as tmp:
                    tmp.write(excel_file.read())
                book = xlrd.open_workbook(path)
                sheet = book.sheet_by_index(0)
                for i in range(1,sheet.nrows):
                    rollno = sheet.cell(rowx=i, colx=0).value
                    fname = sheet.cell(rowx=i, colx=1).value
                    lname = sheet.cell(rowx=i, colx=2).value
                    branch = sheet.cell(rowx=i, colx=3).value
                    email = sheet.cell(rowx=i, colx=4).value
                    phone = sheet.cell(rowx=i, colx=5).value
                    sessions=sheet.cell(rowx=i, colx=6).value
                    token = sheet.cell(rowx=i, colx=7).value
                    # print(rollno,fname,lname,branch,email,phone,sessions,token)
                    rollno,fname,lname,branch,email,phone,sessions,token=str(int(rollno)),fname.strip(),lname.strip(),branch.strip(),email.strip(),str(int(phone)).strip(),sessions.strip(),str(token).strip()
                    # print(rollno,fname,lname,branch,email,phone,sessions,token,"\n\n\n\n\n\n")
                    AlreadyExist=User.objects.filter(username=rollno)
                    if not AlreadyExist:
                        obj=User(username=rollno,first_name=fname,last_name=lname,email=email,is_staff=False,is_active=False,is_superuser=False)
                        obj.save()
                        Exobj=ExtendedUser(user=obj,rollno=rollno,branch=branch,phone=phone,token=str(token),sessions=sessions)
                        Exobj.save()
            finally:
                os.remove(path)
        else:
            form = UpdateExcelForm()
        return render(request,'upload.html', {'form':form,'message':message})
    # else:
    #     return error_404_view(request, exception);
