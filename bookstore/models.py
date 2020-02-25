from django.db import models
import datetime as dt


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=30)

    def __str__(self):
        return "{} {} {} {}".format(self.id,
                                 self.first_name,
                                 self.last_name,
                                 self.date_of_birth)

    def __repr__(self):
        return "{} {} {} {}".format(self.id,
                                 self.first_name,
                                 self.last_name,
                                 self.date_of_birth)


class Book(models.Model):
    title = models.CharField(max_length=120)
    author_first_name = models.CharField(max_length=20)
    author_last_name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    book_description = models.TextField(max_length=10000)
    buyer_id = models.DecimalField(max_digits=4, decimal_places=0, null=True)

