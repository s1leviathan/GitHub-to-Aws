
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('chatbox.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('chat/', include('chat.urls')),  
]

