from django.contrib import admin
from taskapp.models import organization,department,designation,employee,empac

# Register your models here.
class organizationadmin(admin.ModelAdmin):
    list_display =["cname","cemployees","cid","caddr","cedate"]
admin.site.register(organization,organizationadmin)

class departmentadmin(admin.ModelAdmin):
    list_display =["department"]
admin.site.register(department,departmentadmin)

class designationadmin(admin.ModelAdmin):
    list_display =["designation"]
admin.site.register(designation,designationadmin)

class employeeadmin(admin.ModelAdmin):
    list_display =["ename","eno","esal","etech","eaddr","email","emobileno"]
admin.site.register(employee,employeeadmin)

class empacadmin(admin.ModelAdmin):
    list_display =["elogin","elogout","breakhourstart","breakhourend"]
admin.site.register(empac,empacadmin)