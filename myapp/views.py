from django.shortcuts import render, HttpResponse,redirect
from myapp.models import User_Data
# Create your views here.

def SignIn(request):
    if request.method == "POST":
        try :
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username,password)
            if User_Data.objects.filter(username=username)[0].password==password:
                print("valid user")
                return render(request, 'homepage',context={})
            else :
                print("invalid user")
        except Exception as error:
            print(error)
    return render(request, 'login.html' )

def homepage(request):
    return render(request,'homepage.html')
    
def SignUp(request):
    if request.method == "POST":
        try :
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            # password = make_password(request.POST.get('password'))
            print(firstname,lastname,username,email,password)
            newuser = User_Data.objects.create(first_name=firstname,last_name=lastname,email=email,password=password,username=username)

            return redirect('/')
        except Exception as error:
            print(error)
        
    return render(request,'signup.html')