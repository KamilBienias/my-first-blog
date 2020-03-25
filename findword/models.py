from django.db import models


class Findword(models.Model):
    text = models.TextField(max_length=10000)
    phrase = models.CharField(max_length=100)
