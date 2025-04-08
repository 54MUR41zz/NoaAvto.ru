"""
URL configuration for test_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . import Sign_Up

auth = [
    path("accounts/SignIn/", auth_views.LoginView.as_view()),
    path("accounts/logout/", auth_views.LogoutView.as_view()),
    path("accounts/SignUp/", Sign_Up.signup),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name = "index"),
    path("SignUp/", views.SignUp, name = "index"),
    path("SignIn/", views.SignIn, name = "index"),
    path("SignUp/myprofile/", views.profile, name = "index")
] + auth
