from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,"login.html")
def signup(request):
    return render(request,"signup.html")
def home(request):
    return render(request,"home.html")
def compose(request):
    return render(request,"compose.html")
def profile(request):
    return render(request,"profile.html")
