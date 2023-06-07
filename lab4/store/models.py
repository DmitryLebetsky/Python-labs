from django.db import models
from django.urls import reverse

# Create your models here.

class RealtyType(models.Model) :
    
    name = models.CharField(max_length=200,
                             help_text='Enter realty type')
    
    def get_absolute_url(self):
        return reverse('store:realty_list_by_category', args=[str(self.name)])
    
    def __str__(self) :
        return self.name
    
class Realty(models.Model) :

    name = models.CharField(max_length=200)
    owner = models.ForeignKey('Owner',
                                    on_delete = models.SET_NULL,
                                    null = True)
    cost = models.IntegerField()
    type = models.ForeignKey('RealtyType',
                                on_delete = models.SET_NULL,
                                null = True)
    description = models.TextField()
    image = models.ImageField(upload_to='realty/%Y/%m/%d', blank=True)
    

    def get_absolute_url(self):
        return reverse('store:realty_detail', args=[str(self.id)])

    def __str__(self) :
        return self.name   

class Client(models.Model) :

    first_name = models.CharField(max_length=200,
                                help_text='Enter first name')
    last_name = models.CharField(max_length=200,
                                help_text='Enter last name')

    city = models.CharField(max_length=100,
                            help_text='Enter client city') 
    address = models.CharField(max_length=100,
                               help_text='Enter client address')
    phone_number = models.CharField(max_length=50,
                                    help_text='Enter phone number')
    
    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])

    def __str__(self) :
        return '{0}, {1}'.format(self.first_name, self.last_name) 


class Owner(models.Model):
    name = models.CharField(max_length=200,
                            help_text='Enter owner')

    def get_absolute_url(self):
        return reverse('owner-detail', args=[str(self.id)])

    def __str__(self) :
        return self.name 
