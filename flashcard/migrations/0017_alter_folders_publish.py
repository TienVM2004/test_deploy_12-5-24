# Generated by Django 4.1.13 on 2024-05-12 09:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0016_alter_folders_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folders',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 12, 9, 57, 4, 540063, tzinfo=datetime.timezone.utc)),
        ),
    ]
