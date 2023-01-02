from .forms import *
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


#=========================CANDIDATE REGISTRATION=========================
def CandidateRegisterPage(request):
    form = CandidateRegisterForm(request.POST or None)
    if form.is_valid():
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')

        if password1 == password2:
            #Create canidate user objects
            candidate = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
            candidate.save()
            messages.success(request, ('Candidate has been successfully added Please Login'))
            return redirect('login')
        else:
            messages.error(request,'Password not match')
    ctx={
        'form':form,
    }
    return render(request, 'registration/candidate.html',ctx)


#=========================COMPANY REGISTRATION=========================
def CompanyRegisterPage(request):
    form = CompanyRegistrationForm(request.POST or None)
    if form.is_valid():
        first_name = form.cleaned_data.get('first_name')
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        is_staff = form.cleaned_data.get('is_staff')

        if password1 == password2:
            company = User.objects.create_user(first_name=first_name,username=username, email=email,password=password1, is_staff=is_staff)
            company.save()
            messages.success(request, ('Company is created Succesfully! Login Now'))
            return redirect('login')
        else:
            messages.error(request, 'Password not match')
    ctx={
        'form':form,
    }
    return render(request, 'registration/company.html', ctx)


#=========================LOGIN=========================
def LoginPage(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, ('Wrong Credentials'))
    ctx={
        'form':form,
    }

    return render(request, 'registration/login.html', ctx)

#=========================LOGOUT=========================
def LogoutPage(request):
    logout(request)
    return redirect('/')
