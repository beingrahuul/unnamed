from django.shortcuts import render, redirect
from .forms import RegistrationForm, CompleteProfile
from django.contrib.auth import authenticate, login, logout

# Create your views here.

SITE_NAME = 'Unnamed'


def home(request):
    context = {
        'title_name': SITE_NAME
    }

    return render(request, 'unnamed/index.html', context=context)


def User(request):

    context = {
        'text': 'text'
    }

    return render(request, 'unnamed/user.html', context=context)


def CompleteProfilePage(request):

    if request.method == 'POST':
        form = CompleteProfile(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('user')

    else:
        form = CompleteProfile(instance=request.user)

    context = {
        'form': form,
        'Title': 'Complete your profile',
        'user': request.user
    }

    return render(request, 'unnamed/complete.html', context=context)


def ChangeName(request):

    if request.method == 'POST':
        form = CompleteProfile(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('user')

    else:
        form = CompleteProfile(instance=request.user)

    context = {
        'form': form,
        'Title': 'Edit profile',
        'user': request.user
    }

    return render(request, 'unnamed/change_name.html', context=context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('user')

    context = {
        'title_name': 'Login'
    }

    return render(request, 'unnamed/login.html', context=context)


def registerPage(request):
    form = RegistrationForm()

    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('complete_profile')

    context = {

        'title_name': 'Register',
        'form': form
    }

    return render(request, 'unnamed/register.html', context=context)


def logoutUser(request):

    logout(request)
    return redirect('login')

