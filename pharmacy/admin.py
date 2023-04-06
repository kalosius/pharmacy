from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
#Provide access to the admin to the sales
admin.site.register(Sale)