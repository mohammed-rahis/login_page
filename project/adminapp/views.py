from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
def admin_login(request): 
    if 'admin' in request.session:
        
        if 'search' in request.GET:
            search = request.GET['search']
            data = User.objects.filter(username__icontains=search)
        else:
            data =User.objects.all()

        context = {'data' : data}


        return render(request,'admin.html',context)
    else:
        return redirect('/login')


def createuser(request,):

    if request.method == 'POST':        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        confirmpassword = request.POST.get('pass2')

        if password != confirmpassword:
            messages.warning(request,'password not match')
            
        
        try:
            if User.objects.get(Username = username):
                messages.warning(request,'Username is alreay taken')
                
        except:
            pass

        try:
            if User.objects.get(email = email):
                messages.warning(request,'email is alreay taken')
                
        except:
            pass

        myuser = User.objects.create_user(username = username, email = email, password =password)
        myuser.save()
       
        return redirect(admin_login)

    return render(request,createuser)

def deleteuser(request,id): 
    if request.method == 'POST':
        dl = User.objects.get(pk=id)
        dl.delete()
        return redirect(admin_login)
    
    return render(request,deleteuser)

def updateuser(request,id):

    if request.method == 'POST':
             
        username = request.POST.get('username')
        email = request.POST.get('email')

        edit = User.objects.get(id=id)
        edit.username=username
        edit.email=email
        edit.save()

        return redirect(admin_login)
    

    data =User.objects.get(id=id)
    context = {'data' : data}
        
    return render(request,updateuser,context)
 