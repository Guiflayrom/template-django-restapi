import logging

from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers.user_serializer import User, UserSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def initialize_request(self, request, *args, **kwargs):
        request = super().initialize_request(request, *args, **kwargs)
        if request.method == 'POST':
            self.permission_classes = []
        return request


class LogoutView(APIView):
    serializer_class = TokenRefreshSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.info(str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST)
