from django.shortcuts import render, redirect, render_to_response
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from wanderful.models import *
# Create your views here.

def home(request):
    return render_to_response("home.html")

def testing(request):
    return render_to_response("testing.html")
