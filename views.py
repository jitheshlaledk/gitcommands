from django.shortcuts import render,redirect
from django.views.generic import View
from todoapi import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=forms.RegistrationForms()
        return render(request,"registration.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=forms.RegistrationForms(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("signin")
        else:
            return render(request, "registration.html",{"form":form})

class LogInView(View):
    def get(self,request,*args,**kwargs):
        form=forms.LoginForms()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=forms.LoginForms(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                return redirect("home")

            else:
                print("invalid credentials")
                return render(request,"login.html",{"form":form})
        return render(request, "login.html")

class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"home.html")

class LogOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        redirect("signin")







