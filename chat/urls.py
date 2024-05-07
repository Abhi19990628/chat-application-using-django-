from django.urls import path
from .views import home, room, send_message

urlpatterns = [
    path('', home, name='home'),
    path('room/<int:room_id>/', room, name='room'),
    path('room/<int:room_id>/send/', send_message, name='send_message'),
]
