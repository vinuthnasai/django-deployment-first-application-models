from django.db import models
# Create your models here.
class Book(models.Model):
    number=models.IntegerField()
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    published_date=models.DateField()

class Job(models.Model):
    posting_date=models.DateField()
    location=models.CharField(max_length=30)
    offered_salary=models.FloatField()
    qualification=models.CharField(max_length=20)

class Customer(models.Model):
    name=models.CharField(max_length=30)
    cno=models.IntegerField()
    mail_id=models.EmailField()
    phone_number=models.IntegerField()
    age=models.IntegerField()

class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=30)

class Company(models.Model):
    compid=models.IntegerField()
    compname=models.CharField(max_length=30)
    noofemps=models.IntegerField()
    compaddr=models.CharField(max_length=30)
    compsharevalue=models.FloatField()


