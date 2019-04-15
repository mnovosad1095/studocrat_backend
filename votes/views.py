from django.shortcuts import render
from .serializers import VotedPollSerializer
# Create your views here.
from rest_framework import viewsets
from .models import VotedPoll


class VotingView(viewsets.ModelViewSet):
    queryset = VotedPoll.objects.all()
    serializer_class = VotedPollSerializer
