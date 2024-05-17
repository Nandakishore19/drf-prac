import json
from django.shortcuts import render
from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


# Create your views here.
@api_view(["POST","GET"]) # Api home view converted in django rest view 
def api_home(request, *args, **kwargs):
    if request.method != "POST":
        return Response({"detail":"Get not allowed"})
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # print(instance)
        print(serializer.data)
        data = serializer.data
        return Response(data)
