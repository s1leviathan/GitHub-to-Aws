from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404 
from .models import Conversation, Message, UserProfile

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('chatbox')
    else:
        form = AuthenticationForm()
    return render(request, 'chatbox/login.html', {'form': form})

@login_required
def chat_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    conversations = Conversation.objects.filter(participants=user_profile)
    
    return render(request, 'chatbox/chat.html', {'conversations': conversations})

@login_required
def view_conversation(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id)
    messages = Message.objects.filter(conversation=conversation)
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        message_content = request.POST.get('message_content', '')
        
        if message_content:
            user_message = Message.objects.create(conversation=conversation, sender=user_profile, content=message_content)
            sending_message_reply = Message.create_sending_message_reply(conversation, user_profile)

    return render(request, 'chatbox/conversation.html', {'conversation': conversation, 'messages': messages})


@login_required
def chat_list(request):
    user_profile = UserProfile.objects.get(user=request.user)
    conversations = Conversation.objects.filter(participants=user_profile)
    return render(request, 'chatbox/chat_list.html', {'conversations': conversations})

def home_view(request):
    return render(request, 'chatbox/home.html')