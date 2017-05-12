from rest_framework.generics import (
                                    ListAPIView, RetrieveAPIView,
                                    UpdateAPIView,DestroyAPIView,
                                    CreateAPIView,
                                    RetrieveUpdateAPIView, #to auto fill before editing
                                    )

from posts.models import Post
from .serializers import (
    PostListSerializer,
    PostDetailSerializer,
    PostCreateSerializer)

from rest_framework.permissions import (AllowAny,IsAdminUser,
                                        IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from .permissions import IsOwnerOrReadOnly

from rest_framework.filters import (SearchFilter,OrderingFilter)

#from rest_framework.pagination import (LimitOffsetPagination,PageNumberPagination)

from .pagination import (PostLimitOffsetPagination,
                         PostPageNumberPagination)

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

    #to know the user who created the post
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    # for filtering queryset:
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title', 'user__first_name', 'content']

    '''
    note: for filtering with both search and order filter use '&'
    symbol between '?search' and 'ordering' in url
    '''
    pagination_class = PostPageNumberPagination



class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

    # to know the user who updated the post
    def perform_update(self, serializer):
        serializer.save(user= self.request.user)

class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]