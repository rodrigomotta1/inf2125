# Generated by Django 5.1.4 on 2025-01-29 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualizer', '0002_userprofile_saved_places'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='saved_places',
        ),
        migrations.AddField(
            model_name='place',
            name='observers',
            field=models.ManyToManyField(related_name='saved_places', to='visualizer.userprofile'),
        ),
    ]
