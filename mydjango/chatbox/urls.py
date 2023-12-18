
from django.urls import path
from .views import UserListView, ConversationListView, MessageListView, IndexView

app_name = 'chatbox'

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    path('conversations/', ConversationListView.as_view(), name='conversation_list'),
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('', IndexView.as_view(), name='index'),
]