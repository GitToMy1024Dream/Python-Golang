# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=20)


class Contact(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    sex = models.CharField(max_length=10)
    adress = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name


class Tag(models.Model):
    contact = models.ForeignKey(Contact) # Tag以Contact作为外部键
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

