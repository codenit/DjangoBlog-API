from rest_framework.permissions import (AllowAny,IsAdminUser,
                                        IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from posts.api.permissions import IsOwnerOrReadOnly

from rest_framework.filters import (SearchFilter,OrderingFilter)
from rest_framework.generics import (
                                    ListAPIView, RetrieveAPIView,
                                    UpdateAPIView,DestroyAPIView,
                                    CreateAPIView,
                                    RetrieveUpdateAPIView, #to auto fill before editing
                                    )
from .serializers import (UserCreateSerializer)
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
