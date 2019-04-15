from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('votes', views.VotingView)

urlpatterns = [
    path('votes/', include(router.urls))
]
