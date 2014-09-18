from django.shortcuts import render, redirect, render_to_response

# Create your views here.
#test github

def home(request):
    return render_to_response("home.html")

def test(request):
    return render_to_response("test.html")