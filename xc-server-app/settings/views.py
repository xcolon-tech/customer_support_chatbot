from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import UserSettings
from .serializers import UserSettingsSerializer

class UserSettingsView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSettingsSerializer
    queryset = UserSettings.objects.all()

    def get_object(self):
        return self.request.user.settings

class UploadProfilePictureView(generics.UpdateAPIView):
    serializer_class = UserSettingsSerializer
    queryset = UserSettings.objects.all()
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self):
        return self.request.user.settings

    def patch(self, request, *args, **kwargs):
        data = {'bot_profile_picture': request.data.get('bot_profile_picture')}
        serializer = self.get_serializer(instance=self.get_object(), data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)