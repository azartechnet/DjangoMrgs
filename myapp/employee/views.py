from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("welcome to the Employee App")
def about(request):
    return HttpResponse("This is about us")
def contact(request):
    return render(request,"contact.html")
def login_view(request):
    return render(request,"login.html")
