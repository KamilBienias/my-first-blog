from django.db import models


class Search(models.Model):
    website_address = models.URLField(max_length=1000)
    passed_expression = models.CharField(max_length=100)
