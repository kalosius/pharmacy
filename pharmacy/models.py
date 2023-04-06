from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#model means description of the space on the database where we store things
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
    
    item_name = models.CharField(max_length =50, null = True, blank = True)
    total_quantity = models.IntegerField(default = 0, null = True, blank = True)
    issued_quantity = models.IntegerField(default = 0, null = True, blank = True)
    received_quantity = models.IntegerField(default = 0, null = True, blank = True)
    unit_price = models.IntegerField(default = 0, null = True, blank = True)
    manufacturer = models.CharField(max_length=50, null = True, blank = True)
    brand = models.CharField(max_length=50, null = True, blank = True)
    def __str__(self):
        return self.item_name
    
class Sale(models.Model):
    # The item name, the price, purchasers name, date of purchase, quantity purchased
    item = models.ForeignKey( Product, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 0, null = False, blank = True)
    amount_received = models.IntegerField(default = 0, null = False, blank = True)
    issued_to = models.CharField(max_length=50, null = True, blank = True)
    unit_price = models.IntegerField(default = 0, null = False, blank = True)
    #user = models.ForeignKey(User, on_delete = models.CASCADE)
    #date = models.DateTimeField(auto_now_add = True)
    
    #the method below calculates the total sale
    def get_total(self):
        total = self.quantity * self.item.unit_price
        return int(total)
    
    #calculate the change using the method below

    def get_change(self):
        change = self.get_total() - self.amount_received
        return abs(int(change))
    
    # Other fields are added here
    def get_vat(self):
        pass
    
    
    def __str__(self):
        return self.item.item_name


    



    
