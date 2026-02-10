# Ex01 Django ORM Web Application
# Date:7/2/26
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# ENTITY RELATIONSHIP DIAGRAM
<img width="987" height="653" alt="1" src="https://github.com/user-attachments/assets/6cfe0fe9-cb7d-4494-8518-800f241fb424" />


# DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 cars

# PROGRAM
```
admin.py
from django.contrib import admin

from.models import Car,CarAdmin

admin.site.register(Car,CarAdmin)

#Resgister your models here.

models.py
from django.db import models
from django.contrib import admin

class Car(models.Model):
    car_brand = models.CharField()
    car_model = models.CharField()
    year = models.DateField()
    color = models.CharField()
    engine_type = models.CharField()
    fuel_type = models.CharField()
    transmission = models.CharField()
    seating_capacity = models.IntegerField()
    price = models.CharField()m
    description = models.TextField()

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_brand', 'car_model', 'year', 'color', 'engine_type', 'fuel_type', 'transmission', 'seating_capacity', 'price', 'description')
```

# OUTPUT

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/2648a729-f4c2-48d4-ace0-ec28bfd50919" />

# RESULT
Thus the program for creating a database using ORM hass been executed successfully
