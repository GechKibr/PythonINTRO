from django.db import models

# Create your models here.
class Product(models.Model):
	title       = models.CharField(max_length=100)
	price       = models.DecimalField(decimal_places=3,max_digits=10000)
	description = models.TextField(blank=True,null=True)
	summary     = models.TextField()
	featured    = models.BooleanField(null=True)