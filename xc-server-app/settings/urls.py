from django.urls import path
from .views import UserSettingsView, UploadProfilePictureView

urlpatterns = [
    path('user/', UserSettingsView.as_view(), name='user-settings'),
    path('upload-profile-picture/', UploadProfilePictureView.as_view(), name='upload-profile-picture'),
]