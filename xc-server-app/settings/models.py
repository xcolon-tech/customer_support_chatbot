from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='settings')
    default_language = models.CharField(max_length=10, default='EN')
    bot_profile_picture = models.CharField(max_length=10)
    automated_response = models.BooleanField(default=True)
    personalized_assistance = models.BooleanField(default=True)
    live_chat_support = models.BooleanField(default=True)
    sentiment_analysis = models.BooleanField(default=True)
    faq_bot = models.BooleanField(default=True)
    multi_lingual_support = models.BooleanField(default=True)
    security_compliance = models.BooleanField(default=True)

    def __str__(self):
        return f"Settings for {self.user.username}"