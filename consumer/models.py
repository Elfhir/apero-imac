from django.db import models
from review.models import *

#Consumer
class Consumer(models.Model):
	slug = models.SlugField(max_length=200, blank = True)
	username = models.CharField(max_length=200, blank = True)
	password = models.CharField(max_length=200, blank = True)
	email = models.EmailField(max_length=150, blank = True)
	create_date = models.DateField(auto_now_add=True,  auto_now=False, verbose_name="Date d'inscription")
	reviews = models.ForeignKey(Review, blank = True, null = True)

	def __unicode__(self):
		return self.username


