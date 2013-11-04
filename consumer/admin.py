from django.contrib import admin
from models import *

class ConsumerAdmin(admin.ModelAdmin):
	model = Consumer
	date_hierarchy = 'date_joined'

admin.site.register(Consumer, ConsumerAdmin)

