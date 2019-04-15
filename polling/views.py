from django.shortcuts import render
from .serializers import PollSerializer
# Create your views here.
from rest_framework import viewsets
from .models import Poll


class PollingView(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
