# Generated by Django 2.0.3 on 2018-03-13 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygym', '0003_auto_20180313_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='day',
        ),
        migrations.AddField(
            model_name='day',
            name='excercise',
            field=models.ManyToManyField(to='mygym.Exercise'),
        ),
        migrations.AddField(
            model_name='plan',
            name='day',
            field=models.ManyToManyField(to='mygym.Day'),
        ),
    ]
