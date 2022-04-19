# Generated by Django 3.0.14 on 2022-03-17 16:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 3, 17, 16, 50, 22, 776090, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
