from django.db import models

# Create your models here.
class ContactU(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    emaill= models.CharField(max_length=255)
    message= models.TextField(max_length=255)

class mail(models.Model):
    email2= models.TextField(max_length=255)
