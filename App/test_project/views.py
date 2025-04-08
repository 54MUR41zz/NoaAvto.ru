from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import request
from random import *
from .forms import TestForm

def index(request: HttpRequest):
    return render(request, 'main_page.html')

def SignUp(request: HttpRequest):
    return render(request, 'SignUp.html')

def SignIn(request: HttpRequest):
    return render(request, 'SignIn.html')

def profile(request: HttpRequest):
    if request.POST:
        email = request.POST.get('email')
        gender = request.POST.get('gender')

        return render(request, "profile.html", {
            "id": random.randint(1, 100),
            "email": email,
            "gender": gender,
        })
    else:
        return 404

def test_form(request: HttpRequest):
    if request.POST:
        form = TestForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['text_field']
            print(name)
            # add data to database
            return HttpResponseRedirect("/")
    else:
        form = TestForm()

    return render(request, "test.html", {
        "form": form,
    })