# from django.shortcuts import render,HttpResponse
# from .models import *
# from .video_form import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse
from .models import *
from .video_form import *
from django.contrib.auth import authenticate, login as auth_login
from .backends import EmailAuthBackend
# Create your views here.
def index(request):
    videoss = Videos.objects.all()
    return render(request,'index1.html', {'videos': videoss})

    

# def upload(request):
#     all_videos=Videos.objects.all
#     if request.method== 'POST':
#         form=FileSerializers(data=request.POST,files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("<h1> upload Successfull</h1> ")
#     else:
#         form=FileSerializers()
#     return render(request,'upload.html',{"form":form,"all":all_videos})


def upload(request):
    all_videos = Videos.objects.all()
    if request.method == 'POST':
        form = FileSerializers(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Upload Successful</h1>")
    else:
        form = FileSerializers()

    # form.fields['video_file'].widget.attrs['class'] = 'form-control-file'

    return render(request, 'upload.html', {"form": form, "all": all_videos})



def play1(request,pk):
    video = Videos.objects.get(id=pk)
    return render(request,'play1.html', {'video': video})
def play2(request):
    return render(request,'play2.html')

def list_videos(request):
    videoss = Videos.objects.all()
    return render(request, 'videooss.html', {'videos': videoss})

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

def login(request):

    form = LoginForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password'] 
         
        user = EmailAuthBackend.get_user_by_email(request, email=email)
        uid=User.objects.get(email=email)
        if uid.password==password:
            return redirect('home')
        # if user is not None:
        #     return redirect('home')  
        # else:
        #     error_message = "Invalid email or password."
        #     return render(request, 'login.html', {'form': form, 'error_message': error_message})
    
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)  # Initialize the form with POST data
        if form.is_valid():  # Check if form data is valid
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                auth_login(request, user)
                return redirect('login')  
            except Exception as e:
                form.add_error(None, str(e))
    else:
        form = RegistrationForm()  # Initialize an empty form for GET requests

    return render(request, 'registration.html', {'form': form})


