# Generated by Django 5.1.4 on 2025-01-24 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualizer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='saved_places',
            field=models.ManyToManyField(to='visualizer.place'),
        ),
    ]
