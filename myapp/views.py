from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login as auth_login
from myapp.models import User_Data
from django.contrib import auth
from random import randint
import json
# Create your views here.

def search(request):
    if request.user.is_authenticated:
        interests = User_Data.objects.get(username=request.user.username).interests.split(",")
        print(interests)
        reccomendation = set()
        for interest in interests :
            for user in User_Data.objects.all():
                if interest in user.interests and user.username != request.user.username:
                    print(interest,user.interests)
                    reccomendation.add(user)
        print(reccomendation)
        context = {
            'search_html' : True,
            'Users' : reccomendation,
            # 'interests' : obj.interestsz

        }
        return render(request, 'search.html',context)
    else :
        return render(request,'login.html')
def contact(request):
    if request.user.is_authenticated:
        return render(request, 'contact.html',{'username':request.user.username,'contact_html':True})
    else:
        return render(request,'login.html')

def home(request):
    if request.user.is_authenticated:
        return render(request,'index.html',{'index_html':True})
    else:
        return render(request,'login.html')

def profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
                interests = request.POST.get('interests')
                experiance = request.POST.get('experiance')
                age = request.POST.get('age')
                git = request.POST.get('git')
                bio = request.POST.get('bio')
                linked_in = request.POST.get('linkedin')
                instagram = request.POST.get('instagram')
                username = request.POST.get('username')
                firstname = request.POST.get('firstname')
                lastname = request.POST.get('lastname')
                email = request.POST.get('email')
                user_obj = User_Data.objects.get(username=request.user.username)
                user_obj.interests = interests
                user_obj.experiance = experiance
                user_obj.age = age  
                user_obj. git = git
                user_obj.bio = bio
                user_obj.linked_in = linked_in
                user_obj.instagram = instagram
                user_obj.username = username
                user_obj.save()
                user_obj2 = User.objects.get(username=request.user.username)
                user_obj2.username = username
                user_obj2.first_name = firstname
                user_obj2.last_name = lastname
                user_obj2.email = email
                user_obj2.save()
                obj = User_Data.objects.get(username=request.user.username)
                context = {
                    'interests' : obj.interests,
                    'experience' : obj.experiance,
                    'age' : obj.age,
                    'git' : obj.git,
                    'bio' : obj.bio,
                    'linkedin' : obj.linked_in,
                    'instagram' : obj.instagram,
                    'username' : request.user.username,
                    'firstname' : User.objects.get(username=request.user.username).first_name,
                    'lastname' : User.objects.get(username=request.user.username).last_name,
                    'email' : User.objects.get(username=request.user.username).email,
                    'message' : 'Profile Updated Successfully',
                    'index_html' : True,
                }
                return render(request,'index.html',context=context)
            except Exception as error:
                print(error)
                return render(request,'profile.html',{'error':error,'profile_html':True})
        obj = User_Data.objects.get(username=request.user.username)
        context = {
            'interests' : obj.interests,
            'experience' : obj.experiance,
            'age' : obj.age,
            'git' : obj.git,
            'bio' : obj.bio,
            'linkedin' : obj.linked_in,
            'instagram' : obj.instagram,
            'username' : request.user.username,
            'firstname' : User.objects.get(username=request.user.username).first_name,
            'lastname' : User.objects.get(username=request.user.username).last_name,
            'email' : User.objects.get(username=request.user.username).email,
            'profile_html':True,
        }
        return render(request,'profile.html',context=context)
    else:
        return render(request,'login.html')

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
            print("User successfully created : "+username)
            redirect('/',{'message':'Account Created Successfully.'})
        except Exception as error:
            print(error)
            render(request, 'login.html',{'error':error})


#   here is the code for signin and login user
    if request.method == "POST" and request.POST.get('signin') == "":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username,password=password)

            if user and user.is_active:
                auth_login(request,user)
                context = {'name':username,'index_html':True}
                return redirect('home')
            else :
                return render(request,'login.html',{'message':'NotValid'})
                
        except Exception as error:
            print(error)
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')








