from django.contrib import admin
from models import *

class DrinkAdmin(admin.ModelAdmin):
	model = Drink
	date_hierarchy = 'create_date'

admin.site.register(Drink, DrinkAdmin)
