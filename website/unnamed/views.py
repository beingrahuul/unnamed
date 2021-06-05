from django.shortcuts import render, redirect
from .forms import RegistrationForm, CompleteProfile, ImageUploadForm
from django.contrib.auth import authenticate, login, logout
from .models import UserData, ImageModel
# Create your views here.

SITE_NAME = 'Unnamed'


def Image(request):

    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            img = form.cleaned_data.get("image")
            obj = ImageModel.objects.create(title=name, img=img)
            obj.save()
            print('hello')
        else:
            form = ImageUploadForm()
    context = {
        'form': ImageUploadForm(),
    }
    return render(request, 'unnamed/image.html', context=context)


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
        form = CompleteProfile(request.POST, request.FILES, instance=request.user)

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
        form = CompleteProfile(request.POST, request.FILES, instance=request.user)

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
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

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
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(request, email=email, password=password)
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


def Search(request):

    context = {}

    if request.method == "GET":

        search_query = request.GET.get("q")

        if len(search_query) > 0:

            search_result = UserData.objects.filter(email__icontains=search_query)\
                .filter(username__icontains=search_query).distinct()

            accounts = []

            for account in search_result:

                accounts.append((account, False))

            context['accounts'] = accounts

    return render(request, 'unnamed/search.html', context=context)