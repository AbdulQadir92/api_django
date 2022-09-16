from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_products, name='get_products'),
    path('add', views.add_product, name='add_product'),
    path('get/<int:id>', views.get_product, name='get_product'),
    path('update/<int:id>', views.update_product, name='update_product'),
    path('delete/<int:id>', views.delete_product, name='delete_product')
]