from django.urls import __path__
from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('vote-poll/<str:pk>/', views.votePoll, name='vote-poll'),
    path('poll-result/<str:pk>/', views.pollResult, name='poll-result'),
    path('create-poll/', views.createPoll, name='create-poll')
]
