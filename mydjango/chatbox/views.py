
from django.shortcuts import render
from django.views.generic import ListView
from .models import Users, Conversation, Messages, IndexContent

class UserListView(ListView):
    model = Users
    template_name = 'chatbox/user_list.html'
    context_object_name = 'users'

class ConversationListView(ListView):
    model = Conversation
    template_name = 'chatbox/conversation_list.html'
    context_object_name = 'conversations'

class MessageListView(ListView):
    model = Messages
    template_name = 'chatbox/message_list.html'
    context_object_name = 'messages'

class IndexView(ListView):
    model = IndexContent 
    template_name = 'chatbox/index.html'