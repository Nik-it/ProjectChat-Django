# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('chat/', include('chat.urls')),
    path('feedback/', include('feedback.urls')),
    path('', include('chat.urls')),  # Redirect home to chat for simplicity
    path('recommendations/', include('recommendations.urls')),
]