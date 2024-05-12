from django.shortcuts import render,redirect
from .models import *
from .forms import MediaForm
# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):

    if request.POST:

        email=request.POST['email']
        password=request.POST['password']

        uid=User.objects.get(email=email)

        if uid.password==password:

            # con={
            #     'uid' : uid
            # }

            return render(request,'register.html')
        else:

            return render(request,'login.html')
        
    else:

        return render(request,'login.html')


def register(request):

    if request.POST:

        email=request.POST['email']
        name=request.POST['name']
        password=request.POST['password']
        
        uid=User.objects.create(email=email,
                                name=name,
                                password=password)
        return render(request,'register.html')
    else:
        return render(request,'register.html')


def upload(request):

    if request.POST:

        form=MediaForm(request.POST,request.FILES)

        if form.is_valid():

            form.save()

            return redirect(upload)
        
    else:

        form=MediaForm()

        return render(request,'upload.html',{'form':form})


 