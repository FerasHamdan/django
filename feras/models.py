from django.db import models
from django_countries.fields import CountryField

from django.urls import reverse
# Create your models here.

class Auther(models.Model):
    name=models.CharField(max_length=14)
    country=CountryField(blank_label='select country')
    image=models.ImageField(upload_to='images',default='feras.png')


    def __str__(self): 
        return self.name
    def get_url(self):
        return  reverse('details',kwargs={'pk':self.pk})  

    class Meta:
        ordering=['name']    


class articale(models.Model):
    title=models.CharField(max_length=14)
    content=models.TextField(max_length=200)
    auther=models.ForeignKey(Auther,on_delete=models.CASCADE,related_name="articales")


    def __str__(self):
        return self.title


    class Meta:
        ordering=['title']    
