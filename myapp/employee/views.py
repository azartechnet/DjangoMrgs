from django.shortcuts import get_object_or_404, render,redirect

import employee
from employee.models import Employee
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
def list_employees(request):
    from .models import Employee
    employees = Employee.objects.all()
    return render(request, "employee_list.html", {"employees": employees})
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm

def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employees")  # redirect after update
    else:
        form = EmployeeForm(instance=employee)

    return render(request, "employee.html", {"form": form})

def delete_employee(request,id):
    employee=get_object_or_404(Employee,id=id)
    employee.delete()
    return redirect("employees")

