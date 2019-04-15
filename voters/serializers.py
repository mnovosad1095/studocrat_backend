from rest_framework import serializers
from .models import Voter


class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = ('id', 'tg_id', 'faculty', 'year', 'gender', 'polls_voted')
