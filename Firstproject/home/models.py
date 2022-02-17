from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    desc=models.CharField(max_length=122)
    date=models.DateField()

class Blog(models.Model):
    title=models.CharField(max_length=122)
    desc=models.TextField()
    user_id=models.IntegerField(max_length=122)
    username=models.CharField(max_length=122)
    date=models.DateField()