# Generated by Django 4.2 on 2023-05-11 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default='2023-05-11 21:52:29'),
        ),
    ]
