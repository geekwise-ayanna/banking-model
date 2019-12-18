from django.shortcuts import render
from Bank.models import Account, Product
from rest_framework import viewsets
from Bank.serializers import AccountSerializer, ProductSerializer

# Create your views here.
class AccountViewset(viewsets.ModelViewSet):
    queryset = Account.objects.all().order_by('-date_joined')
    serializer_class = AccountSerializer

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
