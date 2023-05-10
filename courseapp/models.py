from django.db import models

# Create your models here.
class addcoursedetails(models.Model):
    firstname=models.CharField(max_length=255) #column name
    lastname=models.CharField(max_length=255)
    studentid=models.IntegerField()
    emailid=models.EmailField()
    qualification=models.CharField(max_length=255)
    maincourse=models.CharField(max_length=255)
    alternatecourse=models.CharField(max_length=255)
    image=models.ImageField(upload_to="image/",null=True)
    date=models.DateField()

class addstudentdetails(models.Model):
    firstname=models.CharField(max_length=255) #column name
    lastname=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    studentid=models.IntegerField()
    gender=models.CharField(max_length=255)
    age=models.IntegerField()
    emailid=models.EmailField()
    mobile=models.CharField(max_length=255)
    parentname=models.CharField(max_length=255)
    parentmobile=models.CharField(max_length=255)
    image=models.ImageField(upload_to="image/",null=True)
    date=models.DateField()
