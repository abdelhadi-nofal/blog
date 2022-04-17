from enum import auto
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField


# Create your models here.


class Artical(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    source = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True )
    published_at = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.title