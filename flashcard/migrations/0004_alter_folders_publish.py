# Generated by Django 4.1.13 on 2024-04-10 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0003_remove_studyset_author_alter_folders_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folders',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 10, 14, 39, 51, 376281, tzinfo=datetime.timezone.utc)),
        ),
    ]