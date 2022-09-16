from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)