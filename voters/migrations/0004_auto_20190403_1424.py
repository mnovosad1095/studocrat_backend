# Generated by Django 2.2 on 2019-04-03 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0003_voter_polls_voted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='polls_voted',
            field=models.TextField(default=''),
        ),
    ]