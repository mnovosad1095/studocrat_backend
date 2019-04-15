from django.db import models


class Voter(models.Model):
    tg_id = models.CharField(max_length=30)
    faculty = models.CharField(max_length=30)
    gender = models.CharField(max_length=30, default='No gender')
    year = models.IntegerField(default=1)
    polls_voted = models.TextField(default='none')
