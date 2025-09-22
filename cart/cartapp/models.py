from django.db import models
from django.contrib import admin
class Cart(models.Model):
    cart=models.CharField()
    cart_price=models.IntegerField()
    expiry_date=models.IntegerField()
    ratings=models.IntegerField()
    quantity=models.IntegerField()

class CartAdmin(admin.ModelAdmin):
    list_display=('cart','cart_price','ratings','expiry_date','quantity')

