# Generated by Django 2.0.2 on 2018-03-07 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ui_app', '0004_auto_20180307_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='author',
        ),
    ]
