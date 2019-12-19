from rest_framework import serializers
from Bank.models import Account
from Bank.models import Product


class AccountSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
        model = Account
        fields = ('account name', 'account type', 'account balance')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
        model = Product
        fields = ('product type', 'loan balance', 'loan amount due')
