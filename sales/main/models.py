from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    address = models.TextField(verbose_name='Адрес', blank=True, null=True)
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', blank=True, null=True)
    announcements = models.IntegerField(verbose_name='Количество объявлений', default=0)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Announcement(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    price = models.CharField(max_length=15, verbose_name='Цена')
    created = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')

    def save(self, *args, **kwargs):
        if self.author.announcements == 0:
            self.author.announcements += 1
            self.author.save()
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['created']
