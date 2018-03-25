from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    description = models.TextField()




class Address(models.Model):
    city = models.CharField(max_length=32)
    street = models.CharField(max_length=32)
    house_number = models.IntegerField()
    apartment_number = models.IntegerField()



class Phone(models.Model):
    number = models.IntegerField()
    number_type = models.CharField(max_length=32)


class Email(models.Model):
    email = models.EmailField()


class Groups(models.Model):
    name = models.CharField(max_length=32)
