from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Address(models.Model):
    address1 = models.CharField(max_length=1000)
    address2 = models.CharField(max_length=1000, null=True, blank=True)
    city = models.CharField(max_length=1000)
    state = models.CharField(max_length=1000)
    pincode = models.CharField(max_length=1000)


class School(models.Model):
    name = models.CharField(max_length=1000)
    school_pricipal = models.CharField(max_length=1000)
    address = models.ForeignKey(Address)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    school = models.ForeignKey(School)
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    email_id = models.EmailField(max_length=1000, null=True, blank=True)
    phone_no = models.CharField(max_length=10)


class Student(models.Model):
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    date_of_birth = models.DateField()


class Parent(models.Model):
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    relation = models.CharField(max_length=1000)
    student = models.ForeignKey(Student)
    phone_no = models.CharField(max_length=10)
    address = models.ForeignKey(Address)

