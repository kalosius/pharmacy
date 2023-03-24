from django.db import models

# Create your models here.

#models means description of the space on the database where we store things

#models are python classes

class Category(models.Model):
    name = models.CharField(max_length=50, null = True, blank = True)
    #this gives us a human readable name to represent for the object of the category class
    def __str__(self):  
        return self.name
    
class Product(models.Model):
    # Here we are connecting product model to a category model
    # A foreign key is a column in one table that is being refrenced in another table
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank = True)

    item_names = models.CharField(max_length =50, null = True, blank = True)
    total_quantity = models.IntegerField(default = 0, null = True, blank = True)
    issued_quantity = models.IntegerField(default = 0, null = True, blank = True)
    received = models.IntegerField(default = 0, null = True, blank = True)
    unit_price = models.IntegerField(default = 0, null = True, blank = True)
    manufacturer = models.CharField(max_length=50, null = True, blank = True)
    brand = models.CharField(max_length=50, null = True, blank = True)
    def __str__(self):
        return self.item_names
    