# Generated by Django 2.2 on 2019-04-09 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0007_auto_20190409_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voter',
            name='gender',
        ),
    ]