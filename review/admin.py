from django.contrib import admin
from models import *

class ReviewAdmin(admin.ModelAdmin):
	model = Review
	date_hierarchy = 'create_date'
	
admin.site.register(Review, ReviewAdmin)
