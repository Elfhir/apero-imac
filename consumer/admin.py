from django.contrib import admin
from models import *

class ConsumerAdmin(admin.ModelAdmin):
	model = Consumer
	date_hierarchy = 'create_date'

admin.site.register(Consumer, ConsumerAdmin)

