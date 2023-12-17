
from django.contrib import admin
from django.urls import path, include
from chatbox.views import home_view

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('chat/', include('chat.urls')),  
    path('', home_view, name='home'),
]

