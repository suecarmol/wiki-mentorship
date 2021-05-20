from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    """
    This is for storing data that relates only to accounts on WikiMentor.
    All WikiMentor users have user profiles.
    """

    class Meta:
        app_label = "users"
        verbose_name = "user profile"
        verbose_name_plural = "user profiles"

    # Related name for backwards queries defaults to "userprofile".
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    wp_username = models.CharField(max_length=235, help_text="Wikipedia username")
    wp_registered = models.DateField(
        help_text="Date registered at Wikipedia", blank=True, null=True
    )
    wp_sub = models.IntegerField(
        unique=True, help_text="Wikipedia user ID"
    )  # WP user id.
    wp_editcount = models.IntegerField(help_text="Number of edits user has made")
    wp_blocked = models.BooleanField(
        default=False, help_text="Does the user have any blocks on Wikipedia?"
    )
    app_username = models.CharField(
        max_length=235, help_text="WikiMentor generated username", unique=True
    )
    email = models.CharField(
        max_length=235,
        help_text="User provided email to send notifications",
        null=True,
        blank=True,
    )
    number_of_blocks = models.IntegerField(
        help_text="Number of blocks the user has accumulated in WikiMentor"
    )
    blocked_by = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="blockedby",
        help_text="A list of users that have blocked this user",
    )
    has_blocked = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="hasblocked",
        help_text="A list of users this user has blocked",
    )
