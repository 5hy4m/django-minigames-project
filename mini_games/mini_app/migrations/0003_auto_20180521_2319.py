# Generated by Django 2.0.2 on 2018-05-21 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_app', '0002_auto_20180521_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archery_boards',
            name='score',
            field=models.IntegerField(null=True),
        ),
    ]