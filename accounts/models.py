from django.db import models
from django import forms

class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.title
