from django.db import models


class Search(models.Model):
    website_address = models.URLField(max_length=1000)
    passed_expression = models.CharField(max_length=100)


class Searchtext(models.Model):
    passed_text = models.TextField(max_length=10000)
    passed_phrase = models.CharField(max_length=100)
