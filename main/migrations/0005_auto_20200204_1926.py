# Generated by Django 3.0.2 on 2020-02-04 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_person_query'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listsource',
            name='urlSource',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
