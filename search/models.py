from django.db import models


class Search(models.Model):
    website_address = models.CharField(max_length=100)
    passed_expression = models.CharField(max_length=100)
