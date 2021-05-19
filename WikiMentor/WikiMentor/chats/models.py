from django.db import models

from WikiMentor.topics.models import Topic
from WikiMentor.users.models import UserProfile


class Chat(models.Model):
    class Meta:
        app_label = "chats"
        verbose_name = "chat"
        verbose_name_plural = "chats"

    mentor = models.ForeignKey(
        UserProfile, related_name="mentorchats", on_delete=models.CASCADE
    )
    mentee = models.ForeignKey(
        UserProfile, related_name="menteechats", on_delete=models.CASCADE
    )
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)


class Message(models.Model):
    class Meta:
        app_label = "messages"
        verbose_name = "message"
        verbose_name_plural = "messages"

    chat = models.ForeignKey(Chat, related_name="chats", on_delete=models.CASCADE)
    message_content = models.TextField()
