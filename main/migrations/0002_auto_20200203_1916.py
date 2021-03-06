# Generated by Django 3.0.2 on 2020-02-03 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='query',
            field=models.TextField(null=True, verbose_name='Текст запроса'),
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ResultOfQuery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.RecommendArticle')),
                ('findQuery', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Person', to='main.Person')),
            ],
            options={
                'verbose_name': 'Запрос',
                'verbose_name_plural': 'Запросы',
            },
        ),
    ]
