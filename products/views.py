from django.shortcuts import render
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required


@api_view(["GET"])
def get_category(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=201)


@login_required(login_url='login')
@api_view(["POST"])
def create_category(request):
    # if request.method == "POST":
    serializer = CategorySerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@login_required(login_url='login')
@api_view(["POST"])
def delete_category(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return Response(status=201)


@api_view(["GET"])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=201)



@login_required(login_url='login')
@api_view(["POST"])
def add_product(request):
    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@login_required(login_url='login')
@api_view(["POST"])
def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response(status=201)
