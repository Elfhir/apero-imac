from django.db import models

#Consumer
class Consumer(models.Model):
	slug = models.SlugField(max_length=200)
	username = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	email = models.CharField(max_length=200)

	def __unicode__(self):
		return "%u" % (self.username)
