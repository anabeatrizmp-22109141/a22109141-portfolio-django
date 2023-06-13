# Generated by Django 4.2.1 on 2023-06-05 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='areas',
        ),
        migrations.AddField(
            model_name='author',
            name='areas',
            field=models.ManyToManyField(related_name='autor', to='portfolio.area'),
        ),
    ]
