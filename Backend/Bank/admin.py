from django.contrib import admin
from Bank.models import Account, Product

# class TodoAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'completed') 

# Register your models here.
admin.site.register(Account)
admin.site.register(Product)
