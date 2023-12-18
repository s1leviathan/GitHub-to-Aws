from django.contrib import admin
from .models import Users, Conversation, Messages

admin.site.register(Users)
admin.site.register(Conversation)
admin.site.register(Messages)