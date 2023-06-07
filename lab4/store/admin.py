from django.contrib import admin

from .models import Realty, Owner, RealtyType, Client
# Register your models here.

@admin.register(Realty)
class RealtyAdmin(admin.ModelAdmin) :
    list_display = ['name', 'owner', 'image', 'cost', 'type', 'description']
    list_filter = ['owner', 'type']

@admin.register(Owner)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(RealtyType)
class RealtyTypeAdmin(admin.ModelAdmin) :
    list_display = ['name']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin) :
    list_display = ['first_name', 'last_name', 'address',
                    'city', 'phone_number']
    list_filter = ['city']
    