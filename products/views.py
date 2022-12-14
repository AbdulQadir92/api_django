from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt
import datetime


# Create your views here.
def get_products(request):
    query_set = Product.objects.filter(updated_at=None, deleted_at=None).values()
    products = []
    for product in query_set:
        products.append(product)
    return JsonResponse(products, safe=False)


@csrf_exempt
def add_product(request):
    if request.method == 'POST':

        title = request.POST.get('title')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        
        product_obj = Product.objects.create(title=title, price=price, image=image, created_by=1)
        product = {
            'id': product_obj.id,
            'title': product_obj.title,
            'price': product_obj.price
        }
        return JsonResponse({"product": product, "message": "product created"})
    else:
        return JsonResponse({"error": "Only post method is allowed"})


def get_product(request, id):
    query_obj = Product.objects.get(id=id)
    product = {
        "id": query_obj.id,
        "title": query_obj.title,
        "price": query_obj.price,
        "image": query_obj.image.url
    }
    return JsonResponse(product)


@csrf_exempt
def update_product(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        query_obj = Product.objects.get(id=id)
        query_obj.updated_by = 1
        query_obj.updated_at = datetime.datetime.now()

        if image:
            product_obj = Product.objects.create(title=title, price=price, image=image, created_by=1)
        else:
            product_obj = Product.objects.create(title=title, price=price, image=query_obj.image, created_by=1)

        query_obj.save()    

        product = {
            "id": product_obj.id,
            "title": product_obj.title,
            "price": product_obj.price,
            "image": product_obj.image.url
        }

        return JsonResponse({"product": product, "message": "product updated"})
    else:
        return JsonResponse({"error": "Only post method is allowed"})


@csrf_exempt
def delete_product(request, id):
    if request.method == 'POST':
        query_obj = Product.objects.get(id=id)
        query_obj.deleted_by = 1
        query_obj.deleted_at= datetime.datetime.now()
        query_obj.save()
        return JsonResponse({"message": "product deleted"})
    else:
        return JsonResponse({"error": "Only post method is allowed"})