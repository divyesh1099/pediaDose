from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=100, unique=True)
    formula_min = models.FloatField(null=True, blank=True)
    formula_max = models.FloatField(null=True, blank=True)
    information = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=100, unique=True)
    types = models.ManyToManyField(Type, blank=True)
    information = models.TextField()
    formula_min = models.FloatField(null=True, blank=True)
    formula_max = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name