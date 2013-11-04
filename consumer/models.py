from django.db import models

#Consumer
class Consumer(models.Model):
	slug = models.SlugField(max_length=200)
	username = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	email = models.EmailField(max_length=150)
	date_joined = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.username
