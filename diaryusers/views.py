from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

def userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request,user)
        return redirect("diarycover")

    else:
        form = AuthenticationForm()
        return render(request, 'userlogin.html', {'form' : form})

def userlogout(request):
    logout(request)
    return redirect("diarycover")

def userregister(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
        return redirect("diarycover")
    else:
        form = UserCreationForm
        return render(request, 'usersignup.html', {'form' : form})


