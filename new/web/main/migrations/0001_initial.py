# Generated by Django 4.1.6 on 2023-02-14 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('surname', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=20, verbose_name='Отчество')),
                ('post', models.CharField(choices=[('Директор компании', 'Директор компании'), ('Охранник', 'Охранник'), ('Front-end программист', 'Front-end программист'), ('Back-end программист', 'Back-end программист'), ('Аналитик данных', 'Аналитик данных'), ('Менеджер', 'Менеджер'), ('Главный менеджер', 'Главный менеджер'), ('Главный программист', 'Главный программист'), ('Главный охранник', 'Главный охранник')], max_length=50, verbose_name='Должность')),
                ('emp_date', models.DateField(verbose_name='Дата приема на работу')),
                ('salary', models.FloatField(verbose_name='Заработная плата')),
                ('photo', models.ImageField(default='photos/default.png', upload_to='photos/', verbose_name='Фото')),
            ],
        ),
    ]
