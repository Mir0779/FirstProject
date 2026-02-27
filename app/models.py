from django.db import models
from django.contrib.auth.models import User

class Todo_liste(models.Model):
    designiation= models.CharField(max_length=25,null=True,blank=True)
    contenu = models.CharField(max_length=1000,null=True,blank=True)
    s_done = models.BooleanField(default=False)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)



 
# Create your models here.
