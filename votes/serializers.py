from rest_framework import serializers
from .models import VotedPoll, Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('tg_id', 'faculty', 'year', 'choice')


class VotedPollSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, read_only=False)

    class Meta:
        model = VotedPoll
        fields = ('id', 'poll_name', 'votes')

    def create(self, validated_data):
        vote_data = validated_data.pop('votes')
        voted_poll = VotedPoll.objects.create(**validated_data)
        for i in vote_data:
            Vote.objects.create(poll_id=voted_poll.id, **i)

        return voted_poll

    def update(self, instance, validated_data):
        votes = validated_data.pop('votes')

        instance.poll_name = validated_data.get('poll_name', instance.poll_name)
        instance.save()
        for vote in votes:
            Vote.objects.all().update_or_create(poll_id=instance.id, **vote)

        return instance

