from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    desc=models.CharField(max_length=122)
    date=models.DateField()

class Tag(models.Model):
    title=models.CharField(max_length=56)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title=models.CharField(max_length=122,null=True,default=None)
    desc=models.TextField(null=True,default=None)
    user_id=models.IntegerField(null=True,default=None)
    username=models.CharField(max_length=122,null=True,default=None)
    image=models.ImageField(upload_to='static/images/',null=True,default=None)
    date=models.DateField(null=True,default=None)
    tags=models.ManyToManyField(Tag,related_name='tagss',verbose_name="MyTags",null=True,default=None)
    # tags=models.ForeignKey(Tag,on_delete=models.CASCADE,verbose_name="My Tags",null=True,default=None)




    
