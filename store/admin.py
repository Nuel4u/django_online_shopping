from django.contrib import admin
from .models import Customer ,Product ,Order,OrderItem,ShippingAddress
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user','name','email')


class PriceAdmin(admin.ModelAdmin):
    list_display = ['name','price', 'slug' ,'digital']


admin.site.register(Customer ,CustomerAdmin)
admin.site.register(Product ,PriceAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
