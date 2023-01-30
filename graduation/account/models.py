from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.urls import reverse
from multiselectfield import MultiSelectField

# Create your models here.


class KIDCHOICE(models.Model):

    choice = models.CharField(max_length=154, unique=True)
    def __str__(self):
        return self.choice
class Kindergarden(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    rayon = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    num_free_places = models.IntegerField(default=0,null=True)
    num_register_child=models.IntegerField(default=0,null=True)
    addition= models.ManyToManyField(KIDCHOICE)
    free_places = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('sad',kwargs={'sad_id':self.id})
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Детский садик'
        verbose_name_plural = 'Детские садики'
class Child(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    id_number = models.CharField(max_length=20)
    roditeli = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Родители')
    det_sads = models.ForeignKey('Kindergarden', on_delete=models.CASCADE, verbose_name='Детские сады')
    ochered = models.IntegerField(default=None,null=True)

    def __str__(self):
        return self.name + ' ' + self.surname


    class Meta:
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'

