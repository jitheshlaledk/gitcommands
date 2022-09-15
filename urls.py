from django.urls import path
from todoapi import views


urlpatterns=[
    path("signup",views.SignUpView.as_view(),name="register"),
    path("login",views.LogInView.as_view(),name="signin"),
    path("home",views.HomeView.as_view(),name="home"),
    path("signout",views.LogOutView.as_view(),name="signout")
]

