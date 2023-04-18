from django.urls import path
from pharmacy import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('index/', views.home, name = 'index'),
    path('home/', views.index, name = 'home'),
    path('', auth_views.LoginView.as_view(template_name = 'products/login.html'), name = 'login' ),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'products/logout.html'), name = 'logout' ),
    # this route is for buying [BUY ITEM]
    path('index/<int:product_id>', views.product_detail, name = 'product_detail'),
    path('issue_item/<str:pk>/', views.issue_item, name = 'issue_item'),
    path('add_to_stock/<str:pk>/', views.add_to_stock, name = 'add_to_stock'),
    path('reciept', views.reciept, name='reciept'), 
    path('all_sales/', views.all_sales, name='all_sales' ),
    path('reciept/<int:reciept_id>', views.reciept_detail, name = 'reciept_detail'),
    path('delete/<int:product_id>', views.delete_item, name = 'delete_item'),
    path('services', views.services, name='services')
    

]
# views match request to templates

