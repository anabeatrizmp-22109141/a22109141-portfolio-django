# Generated by Django 4.2.1 on 2023-06-09 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_alter_project_link_repo'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='pessoas',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Pessoa',
        ),
    ]