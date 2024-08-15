from django.urls import path
from .views import ChatHistoryView, SendMessageView

urlpatterns = [
    path('history/', ChatHistoryView.as_view(), name='chat-history'),
    path('send/', SendMessageView.as_view(), name='send-message'),
]