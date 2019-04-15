from django.db import models


class VotedPoll(models.Model):
    poll_name = models.CharField(max_length=50)


class Vote(models.Model):
    choice = models.TextField(default=' ')
    poll = models.ForeignKey(VotedPoll, on_delete=models.CASCADE, related_name='votes')
    faculty = models.CharField(max_length=50)
    year = models.PositiveIntegerField(default=1)
    tg_id = models.CharField(max_length=40, default='00')
