# Generated by Django 2.1.15 on 2021-04-18 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210418_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(blank=True, help_text='use keyboard', null=True),
        ),
    ]
