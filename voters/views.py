from django.shortcuts import render
from .serializers import VoterSerializer
from rest_framework import viewsets
from .models import Voter


class VotingView(viewsets.ModelViewSet):
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer
