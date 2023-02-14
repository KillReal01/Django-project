from django.db import models
from django.utils.html import mark_safe

class Employee(models.Model):
    POSTS = [
        ('Директор компании', 'Директор компании'),
        ('Охранник', 'Охранник'),
        ('Front-end программист', 'Front-end программист'),
        ('Back-end программист', 'Back-end программист'),
        ('Аналитик данных', 'Аналитик данных'),
        ('Менеджер', 'Менеджер'),
        ('Главный менеджер', 'Главный менеджер'),
        ('Главный программист', 'Главный программист'),
        ('Главный охранник', 'Главный охранник')
    ]


    name = models.CharField('Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=20)
    patronymic = models.CharField('Отчество', max_length=20)
    #post = models.CharField('Должность', max_length=50)
    post = models.CharField('Должность', max_length=50, choices=POSTS)
    emp_date = models.DateField('Дата приема на работу')
    salary = models.FloatField('Заработная плата')
    photo = models.ImageField('Фото', upload_to='photos/', default='photos/default.png')

    @property
    def photo_preview(self):
        if self.photo:
            return mark_safe('<img src="{}" width="200" />'.format(self.photo.url))
        return ""

    def __str__(self):
        return (self.surname + ' ' + self.name + ' ' + self.patronymic)

