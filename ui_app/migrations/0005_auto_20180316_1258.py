# Generated by Django 2.0.3 on 2018-03-16 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui_app', '0004_remove_message_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
