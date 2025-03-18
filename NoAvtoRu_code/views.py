from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render


def index(request: HttpRequest):
    result = 0
    text = ""