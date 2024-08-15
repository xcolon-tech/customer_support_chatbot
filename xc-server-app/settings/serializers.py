from rest_framework import serializers
from .models import UserSettings

class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = [
            'default_language', 'bot_profile_picture', 'automated_response', 
            'personalized_assistance', 'live_chat_support', 'sentiment_analysis', 
            'faq_bot', 'multi_lingual_support', 'security_compliance'
        ]