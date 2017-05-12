from rest_framework.serializers import (ModelSerializer,
                                        HyperlinkedIdentityField,
                                        SerializerMethodField)

from posts.models import Post

class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='posts-api:detail',
                                   lookup_field='pk')#by default

    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'title',
            'user',
            'content',
        ]


class PostDetailSerializer(ModelSerializer):
    user = SerializerMethodField()
    html = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'user',
            'id',
            'title',
            'content',
            'html',
            'timestamp',
            'publish',
            'image',
        ]

    def get_user(self,obj):
        return str(obj.user.username)

    def get_html(self,obj):
        return obj.get_markdown()

class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'publish',
            'image'
        ]