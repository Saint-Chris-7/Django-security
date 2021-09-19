from django.http.request import HttpHeaders, HttpRequest
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import StreamingHttpResponse
from .models import User_data
import csv

# Create your views here.
@login_required(login_url="accounts/login")
def index(request):
    devices = User_data.objects.all()
    total_devices = User_data.objects.all().count()
    context = {
        "devices":devices,
        "total_devices":total_devices
        }
    return render(request,"hawk/index.html",context)

class Echo:
    def write(self,value):
        return value

def some_streaming_csv_views(request):
    rows = (["Rows{}".format(idx),str(idx)] for idx in range(6999))
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    return StreamingHttpResponse((writer.writerrow(row) for row in rows),content_type="text/csv",headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},)
       
def registrationView(request):
    if request.method == "POST":
        FirstName= request.POST["FirstName"]
        LastName = request.POST["LastName"]
        username= request.POST["Username"]
        email= request.POST["email"]
        password1 = request.POST["Password1"]
        password2 = request.POST["Password2"]
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
            elif User.objects.filter(email=email):
                messages.info(request,"email already exist")
            else:
                user= User.objects.create_user(username=username,password=password1,email=email,firtname=FirstName,lastname=LastName)
                user.save()  
                messages.success(request,"user created successfully") 
        else:
            messages.info("password already used")
    else:
        return render(request,"/")






    


    
    



        
    
