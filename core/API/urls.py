from django.urls import path
from .auth_views import login, register
from .views import *

urlpatterns = [
    path('auth/login/', login, name='login'),
    path('auth/register/', register, name='register'),
    path('url/create/', create_url, name='create_url'),
    path('url/user/', user_urls, name='user_urls'),
    # delete url
    path('url/delete/<int:pk>/', delete_url, name='delete_url'),
    # get_alerts
    path('url/alerts/', get_alerts, name='get_alerts'),
    # get_requests
    path('url/stats/<int:url_id>/', url_stats, name='url_stats'),
]
