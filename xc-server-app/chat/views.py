from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ChatMessage
from .serializers import ChatMessageSerializer, SendMessageSerializer

class ChatHistoryView(generics.ListAPIView):
    serializer_class = ChatMessageSerializer

    def get_queryset(self):
        user = self.request.user
        return ChatMessage.objects.filter(sender=user).order_by('timestamp')

class SendMessageView(APIView):
    serializer_class = SendMessageSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            message = serializer.save()

            # Simulate a bot response
            bot_response = ChatMessage.objects.create(
                sender=None,  # or a bot user if one exists
                receiver=request.user.username,
                message=f"Bot response to: {message.message}",
            )

            return Response({
                "user_message": ChatMessageSerializer(message).data,
                "bot_response": ChatMessageSerializer(bot_response).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)