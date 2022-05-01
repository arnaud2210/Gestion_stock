from unicodedata import category
from django.db import models


class Category(models.Model):

    category = models.fields.CharField(max_length=100)


class Article(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    label = models.fields.CharField(max_length=200)
    price = models.fields.FloatField()
    quantity = models.fields.IntegerField()
    creation = models.fields.DateField()
