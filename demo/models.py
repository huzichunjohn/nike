from django.contrib.postgres.fields import JSONField, ArrayField
from django.db import models
from bitfield import BitField

class MyModel(models.Model):
    flags = BitField(flags=(
        'awesome_flag',
        'flaggy_foo',
        'baz_bar',
    ))

class Dog(models.Model):
    name = models.CharField(max_length=200)
    data = JSONField()

    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=200)
    tags = ArrayField(models.CharField(max_length=200), blank=True)

    def __str__(self):
        return self.name
