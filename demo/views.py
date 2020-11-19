from django.shortcuts import render
from demo.models import Userdata
from django.contrib import messages

def Indexpage(request):
    return render(request,'index.html')

def Post(request):
    if request.method=='POST':
        name=request.POST["name"]
        email=request.POST["email"]
        passwordd=request.POST["passwordd"]
        Userdata(name=name,email=email,passwordd=passwordd).save()
        messages.success(request,'New User'+  " " +   request.POST['name'] + " " +'Is Saved Successfully !' )
        return render(request,'forms.html')
    else:
        return render(request , "forms.html")

def loginuser(request):
    if request.method=="POST":
        try:
            datauser=Userdata.objects.get(email=request.POST['email'],passwordd=request.POST['passwordd'])
            print("name",datauser )
            request.session['name']=datauser.email
            return render(request,'home.html')
        except Userdata.DoesNotExist:
            messages.success(request, 'Email / Password Invalid..!') 
    return render(request, 'login.html')


            
        
            
                     
        
    return render(request, 'login.html')            
   

    
            
   
              
               
    