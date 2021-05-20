from django.db import models

from WikiMentor.users.models import UserProfile


class Topic(models.Model):
    class Meta:
        app_label = "topics"
        verbose_name = "topic"
        verbose_name_plural = "topics"

    name = models.CharField(max_length=235, help_text="The name of the topic")
    description = models.TextField(help_text="A long description of that topic")
    potential_mentors = models.ManyToManyField(
        UserProfile, related_name="mentors", null=True, blank=True
    )
    potential_mentees = models.ManyToManyField(
        UserProfile, related_name="mentees", null=True, blank=True
    )
