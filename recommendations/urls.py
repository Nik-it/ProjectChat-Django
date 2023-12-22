# recommendations/urls.py
from django.urls import path
from .views import recommended_services, topic_search

urlpatterns = [
    path('recommended-services/', recommended_services, name='recommended_services'),
    path('topic-search/', topic_search, name='topic_search'),
]