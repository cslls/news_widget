# Generated by Django 4.2 on 2023-05-13 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_news_description_news_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
