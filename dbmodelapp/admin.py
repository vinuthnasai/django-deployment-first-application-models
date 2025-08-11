from django.contrib import admin
from dbmodelapp.models import Book, Job, Customer, Employee, Company


class BookAdmin(admin.ModelAdmin):
    list_display=['number','title','author','published_date']

admin.site.register(Book,BookAdmin)

class JobAdmin(admin.ModelAdmin):
    list_display=['posting_date','location','offered_salary','qualification']
admin.site.register(Job,JobAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','cno','mail_id','phone_number','age']

admin.site.register(Customer,CustomerAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eaddr']
admin.site.register(Employee,EmployeeAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['compid','compname','noofemps','compaddr','compsharevalue']
admin.site.register(Company,CompanyAdmin)