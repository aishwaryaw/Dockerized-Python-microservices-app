from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product, User
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializer import ProductSerializer
import random
from .producer import publish
# Create your views here.


class ProductViewSet(viewsets.ViewSet):

    def list(self,request):
        products = Product.objects.all()
        productserializer = ProductSerializer(products,many=True)
        publish('Products listed', productserializer.data)
        return Response(data=productserializer.data,status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_updated',serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def retrieve(self, request,pk = None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request,pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        publish('product_deleted',pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        print(users)
        user = random.choice(users)
        print(user)
        return Response({
            'id':user.id
        })

    



