from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('voters', views.VotingView)

urlpatterns = [
    path('voters/', include(router.urls))
]
