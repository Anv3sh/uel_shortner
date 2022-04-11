from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Url(models.Model):
    shortened_url=models.SlugField(null=False,unique=True)
    long_url=models.CharField(max_length=100)

    def __str__(self):
        return self.shortened_url

    # def get_absolute_url(self):
    #     return reverse('shorten', kwargs={'slug': self.shortened_url})

    class Meta():
        verbose_name_plural='Urls'

class Personalized(models.Model):
    id=models.ForeignKey(User,unique=True,primary_key=True, serialize=False, verbose_name='ID',on_delete=models.CASCADE)
    shortened_url=models.SlugField(null=False,unique=True)
    long_url=models.CharField(max_length=100)

    def __str__(self):
        return self.shortened_url