from django.shortcuts import render
from taskapp.models import organization,department,designation,employee,empac
from taskapp import forms

# Create your views here.
def detailview(request):
    Organization=organization.objects.all()
    Department=department.objects.all()
    Designation=designation.objects.all()
    Employee=employee.objects.all()
    Empac=empac.objects.all()
    return render(request,"taskapp/detail.html",{"Organization":Organization,"Department":Department,"Designation":Designation,"Employee":Employee,"Empac":Empac})

def employeeformview(request):
    form=forms.employeeform()
    if request.method=="POST":
        form=forms.employeeform(request.POST)
        if form.is_valid():
            form.save()
        return employeedetailview(request)
    return render(request,"taskapp/employeeform.html",{"form":form})

def employeedetailview(request):
    employee_list=employee.objects.all()
    #request.session["employee_list"]=employee_list
    #request.session.set_expiry(120)
    print(type(employee_list))
    return render(request,"taskapp/employeelist.html",{"employee_list":employee_list})