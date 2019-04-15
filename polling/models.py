from django.db import models


class Poll(models.Model):

    poll_name = models.CharField(max_length=50)
    poll_question = models.TextField()

    opening_date = models.DateTimeField()
    closing_date = models.DateTimeField()

    def __str__(self):
        return self.poll_name


class Choice(models.Model):
    choice_text = models.CharField(max_length=100)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='choices')


    def __str__(self):
        return self.choice_text
