# Generated by Django 2.1.15 on 2021-05-12 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20210512_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Date',
            field=models.DateTimeField(blank=True),
        ),
    ]
