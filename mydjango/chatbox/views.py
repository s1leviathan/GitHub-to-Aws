from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
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

def chat_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    conversations = Conversation.objects.filter(participants=user_profile)
    
    return render(request, 'chatbox/chat.html', {'conversations': conversations})
