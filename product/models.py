from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=70)
    unit_price=models.IntegerField()
    quantity=models.IntegerField()
    description=models.CharField(max_length=250)