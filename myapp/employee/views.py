from django.shortcuts import render,redirect
from .forms import EmployeeForm
from django.http import HttpResponse

def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def login_view(request):
   if request.method=="POST":
       username=request.POST.get("username")
       password=request.POST.get("password")
       if username=="admin" and password=="123":
           return HttpResponse("LoginSuccess!!!")
       else:
           return render(request,"login.html",{"error":"Invalid"})
   return render(request,"login.html")

def add_employee(request):
    form = EmployeeForm()   # ✅ Always initialize form

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee")  # ✅ correct name

    return render(request, "employee.html", {"form": form})

