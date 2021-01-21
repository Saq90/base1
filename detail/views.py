from django.shortcuts import render
from django.contrib.auth.models import User,auth
# Create your views here.

def detail(request):
    if request.method == 'POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        user=User.objects.create_user(first_name=first_name,last_name=last_name, username=username,email=email,password=password)
        user.save()



    return render (request,'detail.html')