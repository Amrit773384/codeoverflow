from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from myapp.models import User_Data
from django.contrib import auth
# Create your views here.


def contact(request):
    # if request.user.is_authenticated:
        print(request.user.username)
        return render(request, 'contact.html',{'username':request.user.username})

def home(request):
    # if request.user.is_authenticated:
        return render(request,'index.html',{})

def profile(request):
    # if request.user.is_authenticated:
    print(request.user.username)
    if request.method == "POST":
        print(request.user.username)
        try:
            interests = request.POST.get('interests')
            experiance = request.POST.get('experiance')
            age = request.POST.get('age')
            git = request.POST.get('git')
            bio = request.POST.get('bio')
            linked_in = request.POST.get('linkedin')
            instagram = request.POST.get('instagram')
            # username = request.POST.get('username')
            # firstname = request.POST.get('firstname')
            # lastname = request.POST.get('lastname')
            print(request.user.username)
            email = request.POST.get('email')
            user_obj = User_Data.objects.get(username=request.user.username)
            user_obj.interests = interests
            user_obj.experiance = experiance
            user_obj.age = age
            user_obj. git = git
            user_obj.bio = bio
            user_obj.linked_in = linked_in
            user_obj.instagram = instagram
            user_obj.save()
            return render(request,'index.html',{})
        except User_Data.DoesNotExist:
            print('user doesnt exist')
            return render(request,'profile.html',{})
        except Exception as error:
            print(error)
            return render(request,'profile.html',{})

    return render(request,'profile.html')

def login(request):
#   we have sign up and sign in on same page so we are using if state to differentiate between them

#   To sign up the user and create user account
    if request.method == "POST" and request.POST.get('signup') == "":
        try :
            username = request.POST.get('username')
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            newuser = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,password=password,username=username)

            # create record in user data table
            User_Data.objects.create(username=username)
            redirect('/',{'message':'Account Created Successfully.'})
        except Exception as error:
            print(error)


#   here is the code for signin and login user
    if request.method == "POST" and request.POST.get('signin') == "":
        try:
            username = request.POST.get('username')
            print(username)
            password = request.POST.get('password')

            user = authenticate(username=username,password=password)

            if user:
                context = {'name':username}
                return render(request, 'index.html',context)
            else :
                return render(request,'login.html',{'message':'NotValid'})
                
        except Exception as error:
            print(error)
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')









# def SignIn(request):
#     if request.method == "POST":
#         try :
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             print(username,password)
#             if User_Data.objects.filter(username=username)[0].password==password:
#                 print("valid user")
#                 return render(request, 'homepage',context={})
#             else :
#                 print("invalid user")
#         except Exception as error:
#             print(error)
#     return render(request, 'login.html' )

# def homepage(request):
#     return render(request,'homepage.html')
    
# def SignUp(request):
#     if request.method == "POST":
#         try :
#             firstname = request.POST.get('firstname')
#             lastname = request.POST.get('lastname')
#             username = request.POST.get('username')
#             email = request.POST.get('email')
#             password = request.POST.get('password')
#             # password = make_password(request.POST.get('password'))
#             print(firstname,lastname,username,email,password)
#             newuser = User_Data.objects.create(first_name=firstname,last_name=lastname,email=email,password=password,username=username)

#             return redirect('/')
#         except Exception as error:
#             print(error)
        
#     return render(request,'signup.html')