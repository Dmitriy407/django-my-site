# Generated by Django 3.2.7 on 2021-10-12 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('native_name', models.CharField(max_length=150, unique=True, verbose_name='Название на родном языке')),
                ('description', models.TextField(verbose_name='Описание')),
                ('opinion', models.TextField(verbose_name='Мое мнение')),
                ('slug', models.SlugField(max_length=160, null=True, verbose_name='Слаг')),
                ('rating', models.IntegerField(choices=[(0, 'Не указан'), (1, 'Хуже некуда'), (2, 'Ужасно'), (3, 'Очень плохо'), (4, 'Плохо'), (5, 'Более-менее'), (6, 'Нормально'), (7, 'Хорошо'), (8, 'Очень хорошо'), (9, 'Великолепно'), (10, 'Шедевр')], default=0, verbose_name='Оценка')),
                ('recomend_to_watch', models.BooleanField(default=False, verbose_name='Рекомендую к ознакомлению')),
                ('is_anime', models.BooleanField(default=False, verbose_name='Аниме')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('native_name', models.CharField(max_length=150, unique=True, verbose_name='Название на родном языке')),
                ('description', models.TextField(verbose_name='Описание')),
                ('opinion', models.TextField(verbose_name='Мое мнение')),
                ('slug', models.SlugField(max_length=160, null=True, verbose_name='Слаг')),
                ('rating', models.IntegerField(choices=[(0, 'Не указан'), (1, 'Хуже некуда'), (2, 'Ужасно'), (3, 'Очень плохо'), (4, 'Плохо'), (5, 'Более-менее'), (6, 'Нормально'), (7, 'Хорошо'), (8, 'Очень хорошо'), (9, 'Великолепно'), (10, 'Шедевр')], default=0, verbose_name='Оценка')),
                ('recomend_to_watch', models.BooleanField(default=False, verbose_name='Рекомендую к ознакомлению')),
                ('is_anime', models.BooleanField(default=False, verbose_name='Аниме')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
