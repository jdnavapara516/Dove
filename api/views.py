from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone
from .models import ChatMessage
from .serializers import ChatMessageSerializer, RegisterSerializer

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"msg":"User Created"})
    return Response(serializer.errors)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMessages(request):
    today = timezone.now().date()
    messages = ChatMessage.objects.filter(timestamp__date=today).order_by('timestamp')
    serializer = ChatMessageSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sendMessage(request):
    ChatMessage.objects.create(
        sender=request.user,
        content=request.data.get('content')
    )
    return Response({"msg":"Message sent"})