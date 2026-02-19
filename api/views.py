from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer

@api_view(['POST'])
def register(request):

    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"msg":"User Created"})

    return Response(serializer.errors)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def home(request):
    return Response({"msg":"Welcome to the API"})