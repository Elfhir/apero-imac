from django.db import models
from product.models import *

class Review(models.Model):
	slug = models.SlugField(max_length=40, blank = True)
	name = models.CharField(max_length=40, blank = True)
	content = models.TextField(blank = True, null = True)
	grade = models.DecimalField(max_digits=1, decimal_places=0, blank = True, null = True)
	create_date = models.DateField(auto_now_add = True, auto_now=False, verbose_name="Date de publication")
	product = models.OneToOneField(Product, blank = True, null = True)

	def __unicode__(self):
		return u'%s %s' % (self.name, self.content)

