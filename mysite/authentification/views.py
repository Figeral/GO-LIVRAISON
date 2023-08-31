from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from stock.views import all_category

def log_in(request):
    user=None
    username=None
    context=None
    nouser=None
    if request.user.is_authenticated:
        user=request.user
        return render(request,'template/authentification/user_detail.html',{'user':user})
    else:
          if request.method == 'POST' :
             email=request.POST['email']
             password=request.POST['pw']
             user=authenticate(username="",email=email,password=password)
             if user is not None:
               login(request,user)
               username=user.get_username
               context={
                    'username':username,
                    'user':user}
             else:
                 nouser="user does'nt exit"
             return redirect('stock:all_category')

    
          return render(request,'template/authentification/login.html',context)
    return redirect('')
# there is a problem with the log_in at the parth of the return , since the server redirect to another but the return 
# redirect is invalid . result, the server returns nowhere . try resolve the semantique error i.e program and don't code
    
def signin(request):
    myuser=None
    if request.method == "POST" :
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['pw']
        cpw=request.POST['cpw']
        
        myuser=User.objects.create_user(username=fname+lname,email=email,password=password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,'account created with success')
        return redirect('stock:all_category')
        
    return render(request,'template/authentification/signin.html',{
        'myuser':myuser,
    })
# the same error goes here, read the documentation on http response 
def log_out(request):
     logout(request)
     messages.add_message(request, messages.SUCCESS, f'{request.user.username} logged out successfully')
     return redirect("")
    