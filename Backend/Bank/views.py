from django.shortcuts import render
from rest_framework import viewsets
from Bank.serializers import AccountSerializer, ProductSerializer
from Bank.models import Account, Product

# Create your views here.
class AccountViewset(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
