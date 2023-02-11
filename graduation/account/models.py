
from PIL import Image
from django.contrib.auth.models import  AbstractUser
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.urls import reverse

from multiselectfield import MultiSelectField


# Create your models here.

class User(AbstractUser):
    address = models.CharField(max_length=150,verbose_name='Адрес', unique=True)
    phone = models.IntegerField(blank=True, null=True,verbose_name='Номер телефон')
    email = models.EmailField(blank=True,verbose_name='Имейл')

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Родитель'
        verbose_name_plural = 'Родители'



class KIDCHOICE(models.Model):
    choice = models.CharField(max_length=154, unique=True)

    def __str__(self):
        return self.choice

    class Meta:
        verbose_name = 'Допалнительный кружок'
        verbose_name_plural = 'Допалнительные кружки'

_MAX_SIZE = 300
class Kindergarden(models.Model):
    AREA = [
        ('Lasnamae', 'Lasnamae'),
        ('Kristiine', 'Kristiine'),
        ('Noome', 'Noome')
    ]
    name = models.CharField(max_length=20,verbose_name='Имя')
    address = models.CharField(max_length=255,verbose_name='Адрес')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, max_length=50,verbose_name='Фото')
    area = models.CharField(max_length=30,choices=AREA,verbose_name='Район')
    phone_number = models.CharField(max_length=20,verbose_name='Номер телефона')
    num_free_places = models.IntegerField(default=0, null=True,verbose_name='Количество свободных мест')
    num_register_child = models.IntegerField(default=0, null=True,verbose_name='Кол-во заргис. детей')
    addition = models.ManyToManyField(KIDCHOICE,verbose_name='Доп. кружки')
    free_places = models.BooleanField(default=True,verbose_name='Свободные места')


    def save(self, *args, **kwargs):
        super(Kindergarden, self).save(*args, **kwargs)

        if self.photo:
            filepath = self.photo.path
            width = self.photo.width
            height = self.photo.height
            print(width)
            print(height)

            max_size = max(width, height)
            print(max_size)
            if max_size > _MAX_SIZE or max_size < _MAX_SIZE:
                image = Image.open(filepath)
                print(filepath)
                # resize - безопасная функция, она создаёт новый объект, а не
                # вносит изменения в исходный, поэтому так
                image = image.resize(
                    (round(width / max_size * _MAX_SIZE),
                     round(height / max_size * _MAX_SIZE)),
                    Image.ANTIALIAS
                )
                print(image)
                # И не забыть сохраниться
                image.save(filepath)

    def get_absolute_url(self):
        return reverse('sad', kwargs={'sad_id': self.id})

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
    ochered = models.IntegerField(default=None, null=True)

    def __str__(self):
        return self.name + ' ' + self.surname

    class Meta:
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'
