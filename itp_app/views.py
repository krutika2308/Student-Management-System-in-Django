from django.shortcuts import render,redirect
from .models import itpStudent
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            errormessage = "Username already exists. Please choose a different username."
            return render(request, 'home.html', {"error_message": errormessage})

    
        user=User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        return redirect('user_login')  
    return render(request, 'home.html')


def user_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,"Username not exits.")
            return redirect('user_login')
            
        user = authenticate(username=username , password=password)
        if user is None:
            messages.error(request, "Invalid password")
            return redirect('user_login')
        else:
            login(request,user)
            return redirect("addStudent")
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect("user_login")

# Create your views here.
@login_required(login_url="user_login")
def add_student(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        description=request.POST['description']
        Image=request.FILES.get('Image')

        itpStudent.objects.create(name=name,age=age,description=description,Image=Image)
    return render(request,'add_student.html')


def student_list(request):
    student=itpStudent.objects.all()
    if request.GET.get('search'):
        student=student.filter(name__icontains=request.GET.get('search'))
    return render(request,'student_list.html',{'student':student})



def update_student(request,id):
    student = itpStudent.objects.get(id=id)

    if request.method == 'POST':
        student.name=request.POST.get('name')
        student.age=request.POST.get('age')
        student.description=request.POST.get('description')

        if request.FILES.get('Image'):        
            student.Image=request.FILES.get('Image')

        student.save()
        return redirect('student_list')
    return render(request,'update_student.html',{'student':student})




def delete(request,id):
    student=itpStudent.objects.get(id=id)
    student.delete()
    return redirect('student_list')



def courses(request):
    return render(request,'courses.html')


def about(request):
    return render(request,'about.html')


def fees(request):
    return render(request, 'fees.html')
def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')