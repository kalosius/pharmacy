# form is an interface where a user creates data
from django.forms import ModelForm

#accesing models inorder to link them to the form
from .models import *

class AddForm(ModelForm):
    class Meta:
        model = Product
        fields = ['received_quantity']
    
    # modeling a form basing on our the model inorder to record the sales

class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['quantity', 'amount_received', 'issued_to']








