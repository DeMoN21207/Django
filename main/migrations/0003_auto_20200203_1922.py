# Generated by Django 3.0.2 on 2020-02-03 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200203_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='query',
            field=models.TextField(blank=True, null=True, verbose_name='Текст запроса'),
        ),
    ]
