from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def get_products(request):
    query_set = Product.objects.all().values()
    products = []
    for product in query_set:
        products.append(product)
    return JsonResponse(products, safe=False)


@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data['title']
        price = data['price']
        product_obj = Product.objects.create(title=title, price=price)
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
        "price": query_obj.price
    }
    return JsonResponse(product)


@csrf_exempt
def update_product(request, id):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data['title']
        price = data['price']

        query_obj = Product.objects.get(id=id)
        query_obj.title = title
        query_obj.price = price
        query_obj.save()

        product = {
            "id": query_obj.id,
            "title": query_obj.title,
            "price": query_obj.price
        }

        return JsonResponse({"product": product, "message": "product updated"})
    else:
        return JsonResponse({"error": "Only post method is allowed"})


@csrf_exempt
def delete_product(request, id):
    if request.method == 'POST':
        query_obj = Product.objects.get(id=id)
        query_obj.delete()
        return JsonResponse({"message": "product deleted"})
    else:
        return JsonResponse({"error": "Only post method is allowed"})