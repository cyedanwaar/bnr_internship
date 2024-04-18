from django.db import models


class Product(models.Model):
    slug = models.SlugField(blank=True)
    name = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(blank=True, decimal_places=2, max_digits=8)
