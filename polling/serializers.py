from rest_framework import serializers
from .models import Choice, Poll


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('choice_text', )


class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ('poll_name', 'poll_question', 'opening_date', 'closing_date', 'choices')
