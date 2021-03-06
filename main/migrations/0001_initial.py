# Generated by Django 3.0.2 on 2020-02-03 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urlArticle', models.SlugField(max_length=100, unique=True)),
                ('descripion', models.TextField(verbose_name='Описание статьи')),
                ('nameofarticle', models.TextField(max_length=150, verbose_name='Название статьи')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Author', models.CharField(max_length=50, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='ListSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namesourse', models.CharField(max_length=50, verbose_name='Имя')),
                ('urlSource', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Источник',
                'verbose_name_plural': 'Источники',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('sourname', models.CharField(max_length=40, verbose_name='Фамилия')),
                ('middlename', models.CharField(max_length=40, verbose_name='Отчество')),
                ('login', models.CharField(max_length=15, unique=True, verbose_name='Логин')),
                ('password', models.CharField(max_length=15, verbose_name='Пароль')),
            ],
            options={
                'verbose_name': 'Логин',
                'verbose_name_plural': 'Логины',
            },
        ),
        migrations.CreateModel(
            name='RecommendArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Article')),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Author')),
            ],
            options={
                'verbose_name': 'Рекомендация',
                'verbose_name_plural': 'Рекомендации',
            },
        ),
    ]
