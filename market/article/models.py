from unicodedata import category
from django.db import models


class Category(models.Model):

    category = models.fields.CharField(max_length=100)

    def __str__(self):
        
        return f"{self.category}"


class Article(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    label = models.fields.CharField(max_length=200)
    price = models.fields.FloatField()
    quantity = models.fields.IntegerField()
    creation = models.fields.DateField()

    def __str__(self):
        return f"{self.label}, ({self.quantity})"
