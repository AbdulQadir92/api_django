from django.db import models
from base.models import *

# Create your models here.
class Product(BaseModel):
    title = models.CharField(max_length=200)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)