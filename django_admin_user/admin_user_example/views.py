from django.shortcuts import render
from admin_user_example.user_forms import UserForm, UserInformationForm

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def index(request):
    return render(request, "admin_example/index.html")


def register(request):

    registered = False

    if request.method == "POST":
        userForm = UserForm(data=request.POST)
        informationForm = UserInformationForm(data=request.POST)

        if userForm.is_valid() and informationForm.is_valid() :

            user = userForm.save()
            user.set_password(user.password)
            user.save()

            profile = informationForm.save(commit=False)
            profile.user = user

            if "profile_pic" in request.FILES :
                profile.profile_pic = request.FILES["profile_pic"]


            profile.save()
            registered = True

    else:
        userForm = UserForm()
        informationForm = UserInformationForm()
        
        
    return render(request, "admin_example/user_form.html",
        context={"user_form": userForm, "information_form": UserInformationForm, "registered" : registered})



def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else :
                return HttpResponse("Account is inactive!")
        else:
            print("Login detail provided are invalid !")     
            print("Username : {} and Password : {}".format(username, password))
            return HttpResponse("Login details are invalid !")

    else :
        return render(request, 'admin_example\login.html', context={})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))