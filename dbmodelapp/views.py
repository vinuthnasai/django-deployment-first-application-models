from django.shortcuts import render
from dbmodelapp.models import Job, Customer, Book, Company


#Create your views here.
def jobdata(request):
    joblist=Job.objects.all()  #DJ-ORM-Code...
    dict1={'joblist':joblist}
    return render(request, 'dbmodelapp/job.html', context=dict1)


def custdata(request):
    custlist=Customer.objects.all()  #DJ-ORM-Code...
    dict2={'custlist':custlist}
    return render(request, 'dbmodelapp/cust.html', context=dict2)


#Create your views here.
def bookdata(request):
    booklist=Book.objects.all()  #DJ-ORM-Code...
    dict3={'booklist':booklist}
    return render(request, 'dbmodelapp/book.html', context=dict3)

def cumpdata(request):
    cumplist=Company.objects.all()  #DJ-ORM-Code...
    dict4={'cumplist':cumplist}
    return render(request, 'dbmodelapp/company.html', context=dict4)
