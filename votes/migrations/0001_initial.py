# Generated by Django 2.2 on 2019-04-02 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VotedPoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll_name', models.CharField(max_length=50)),
                ('fbf_votes', models.IntegerField()),
                ('humanity_votes', models.IntegerField()),
                ('health_sciences_votes', models.IntegerField()),
                ('apps_votes', models.IntegerField()),
            ],
        ),
    ]
