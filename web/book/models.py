from django.db import models
from django.contrib import admin

class ecommerce(models.Model):
    product_name=models.CharField(max_length=20)
    product_price=models.IntegerField()

class ecommerce_admin(admin.ModelAdmin):
    list_display=['product_name','product_price']
