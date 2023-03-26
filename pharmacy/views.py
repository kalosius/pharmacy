from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from.models import Product
#now we are including our filters from the filters file
from .filters import Product_filters


# Create your views here.
#@login_required
def index(request):
    products = Product.objects.all().order_by('-id')
    product_filter = Product_filters(request.GET,queryset= products)
    products = product_filter.qs
    return render(request,'index.html', {'products':products,'product_filter':product_filter})

    

#@login_required
def home(request):
    return render(request, 'aboutDrwho.html')
