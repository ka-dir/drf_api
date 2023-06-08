from django.urls import path
from .views import PostView
urlpatterns = [
    path('api/posts/', PostView.as_view(), name='post-list'),
]
