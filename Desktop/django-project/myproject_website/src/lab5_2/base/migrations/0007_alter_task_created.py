# Generated by Django 4.0.3 on 2022-03-30 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20220317_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
