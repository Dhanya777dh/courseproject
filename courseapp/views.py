from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from courseapp.models import addcoursedetails, addstudentdetails

# Create your views here.
def demofun(request):
    return render(request,'home.html')

def loginpage(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def add_course(request):
    if request.user.is_authenticated:
        return render(request,'add_course.html')
    return render(request,'login.html')
def add_course_details(request):
    if request.method=='POST':
        finame=request.POST['fname']  #variable name=form name
        laname=request.POST['lname'] # Form name
        studentid=request.POST['studentid']
        email=request.POST['email']
        qualification=request.POST['qualification']
        mcourse=request.POST['maincourse']
        acourse=request.POST['alternatecourse']
        image=request.FILES.get('file')
        date=request.POST['date']
        
        course=addcoursedetails(firstname=finame,
        lastname=laname,
        studentid=studentid,
        emailid=email,
        qualification=qualification,
        maincourse=mcourse,
        alternatecourse=acourse,
        image=image,
        date=date) #variablename=tablename(models column name=variablename,)
        course.save()
    # return render(request,"add_course.html")
        return redirect('add_course')

def add_student(request):
    if request.user.is_authenticated:
        return render(request,'add_student.html')
    return render(request,'login.html')
def add_student_details(request):
    if request.method=='POST':
        finame=request.POST['fname']  #variable name=form name (htmlpage 'name')
        laname=request.POST['lname'] # Form name
        address=request.POST['address']
        studentid=request.POST['studentid']
        gender=request.POST['gender']
        age=request.POST['age']
        email=request.POST['email']
        mobile=request.POST['mobile']
        parname=request.POST['parentname']
        parmobile=request.POST['parentmobile']
        image=request.FILES.get('file')
        date=request.POST['date']
        
        student=addstudentdetails(firstname=finame,
        lastname=laname,
        address=address,
        studentid=studentid,
        gender=gender,
        age=age,
        emailid=email,
        mobile=mobile,
        parentname=parname,
        parentmobile=parmobile,
        image=image,
        date=date) #variablename=tablename(models column name=variablename,)
        student.save()
    # return render(request,"add_course.html")
        return redirect('add_student')
def showstudentdetails(request):
    if request.user.is_authenticated:
        student=addstudentdetails.objects.all()
        return render(request,'show_student.html',{'student':student})
    return render(request,'login.html')

def logout(request):
    if request.user.is_authenticated:
        return render(request,'logout.html')
    return render(request,'login.html')

def usercreate(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        pword=request.POST['pword']
        cpword=request.POST['cpword']
        email=request.POST['email']

        if pword==cpword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username already Exists...!!! Try another name')
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=fname, #auth user column name=page name
                    last_name=lname,
                    username=username,
                    password=pword,
                    email=email)
                user.save()
                print("Successed....")
        else:
            messages.info(request,'Password Doesnt match')
            print("Password is not matching..")
            return redirect('signup')
        return redirect('/')
    else:
        return render(request,'signup.html')

def login1(request):
    if request.method == 'POST':
        username=request.POST['username']
        pword=request.POST['pword']
        user = auth.authenticate(username=username, password=pword) #auth table name=login name
        # request.session["demoid"]=user.id # method -session
        if user is not None:
            auth.login(request, user)
            messages.info(request, f'Welcome {username}')
            return redirect('logout')
        else:
            messages.info(request,'Invalid Username Or Password. Try Again')
            return redirect('loginpage')
    else:
        return redirect('loginpage')   

def logoutpage(request):
    auth.logout(request)
    return redirect('demofun')