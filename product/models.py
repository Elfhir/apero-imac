from django.db import models
from review.models import *

# abstract
class Product(models.Model):
	slug = models.SlugField(max_length=200, blank = True)
	name = models.CharField(max_length=200, blank = True)
	price = models.CharField(max_length=200, blank = True)
	create_date = models.DateField(auto_now_add = True, auto_now=False, verbose_name="Date d'ajout dans l'index")
	
	def __unicode__(self):
		return u'%s %s' % (self.name, self.price)

class Appetizer(Product):
	salt = models.DecimalField(max_digits=1, decimal_places=0)
	fat = models.DecimalField(max_digits=1, decimal_places=0)
	spicy = models.DecimalField(max_digits=1, decimal_places=0)
	sugar = models.DecimalField(max_digits=1, decimal_places=0)

class Drink(Product):
	degree = models.DecimalField(max_digits=1, decimal_places=0)
	volume = models.DecimalField(max_digits=1, decimal_places=0)
	aroma = models.DecimalField(max_digits=1, decimal_places=0)
	sugar = models.DecimalField(max_digits=1, decimal_places=0)
