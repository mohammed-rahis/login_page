from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from adminapp.views import admin_login
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


# Create your views here.
@never_cache
def index(request):
    if 'username' in request.session:
        username=request.user
        return render(request,'index.html',{'username':username})
    return redirect(loginn)

@never_cache
def signup(request):
    if 'username' in request.session:
        return redirect(loginn)
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("pass1")
        confirmpassword = request.POST.get("pass2")
        

        if password != confirmpassword:
            messages.warning(request,'password not match')
            return redirect(signup)
        
        try:
            if User.objects.get(Username = uname):
                messages.warning(request,'Username is alreay taken')
                return redirect(signup)
        except:
            pass

        try:
            if User.objects.get(email = email):
                messages.warning(request,'email is alreay taken')
                return redirect(signup)
        except:
            pass
        myuser = User.objects.create_user(username = uname,email = email,password = password)
        myuser.save()
        return redirect(loginn)
    

    return render(request,'signup.html')

@never_cache
def loginn(request):
    if 'username' in request.session:
        return redirect(index)
    if 'admin' in request.session:
        return redirect('/admin_login')

    
    if request.method == 'POST':
        uname = request.POST.get('username')
        passwordlogin = request.POST.get('password')
        
        myuser = authenticate(username = uname,password = passwordlogin)
        
        if myuser is not None:
            if myuser.is_superuser:
                request.session['admin']=uname
                
                login(request,myuser)
                return redirect(admin_login)

            request.session['username']=uname

            login(request,myuser)
            return redirect(index)
        else:
            messages.success(request,'username/password is invalid')
            return redirect(loginn)

    return render(request,'login.html')

@login_required(login_url='/login')
def loggout(request):
    if 'username' in request.session:
          del request.session['username']
    logout(request)
    return redirect(loginn)


