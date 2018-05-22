from django.db import models

class NewBookManager(models.Manager):
    def get_query_set(self):
        return super(NewBookManager, self).get_query_set().filter(author='Tony')

class Book(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    objects = models.Manager()  # default
    new_objects = NewBookManager()


class MaleManger(models.Manager):
    def get_query_set(self):
        return super(MaleManger, self).get_query_set().filter(sex='M')

class FemaleManger(models.Manager):
    def get_query_set(self):
        return super(FemaleManger, self).get_query_set().filter(sex='W')

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    sex = models.CharField(max_length=1, choices=('M', 'W'))
    people = models.Manager()
    man = MaleManger()
    woman = FemaleManger()