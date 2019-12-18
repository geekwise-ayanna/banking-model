from django.contrib import admin
from Bank.Accounts.models import Account
from Bank.Product.models import Product

# class TodoAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'completed') 

# Register your models here.
admin.site.register(Account)
admin.site.register(Product)
