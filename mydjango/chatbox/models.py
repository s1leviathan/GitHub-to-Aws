from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Conversation(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

class Messages(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)

class IndexContent(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title
