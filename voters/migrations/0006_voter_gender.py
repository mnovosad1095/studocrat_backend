# Generated by Django 2.2 on 2019-04-09 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0005_auto_20190403_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='gender',
            field=models.CharField(default=None, max_length=30),
        ),
    ]