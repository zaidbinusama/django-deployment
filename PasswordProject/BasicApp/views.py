from django.shortcuts import render
from BasicApp.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    return render(request, 'BasicApp/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def registration(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user



            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:

            print(user_form.errors, profile_form.errors)
    else:
            user_form = UserForm()
            profile_form = UserProfileInfoForm

    return render(request, 'BasicApp/registration.html',
                             {'registered': registered,
                             "user_form": user_form,
                             "profile_form": profile_form})






def user_login(request):


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password = password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                print("could not login")
                return HttpResponse('Account not active')

        else:
            return HttpResponse("Invalid login details supplied")


    else:
        return render(request, 'BasicApp/login.html', {})
