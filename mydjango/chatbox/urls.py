from django.urls import path
from .views import user_login, chat_view, view_conversation, chat_list, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', user_login, name='user_login'),
    path('chat/', chat_view, name='chat'),
    path('conversation/<int:conversation_id>/', view_conversation, name='view_conversation'),
    path('chat-list/', chat_list, name='chat_list'),
]
