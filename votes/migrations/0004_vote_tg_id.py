# Generated by Django 2.2 on 2019-04-04 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0003_vote_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='tg_id',
            field=models.CharField(default='00', max_length=40),
        ),
    ]