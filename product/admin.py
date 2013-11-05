from django.contrib import admin
from models import *

class ProductAdmin(admin.ModelAdmin):
	model = Product
	date_hierarchy = 'create_date'

admin.site.register(Product, ProductAdmin)
