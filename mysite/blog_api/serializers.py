from rest_framework import serializers
from blog.models import Comment, Post
class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField()
    created = serializers.DateTimeField()

    def create(self, validated_data):
        comment = Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.save()

        return instance


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'id',
            'author',
            'title',
            'body',
            'created',
            'status',
            'slug'
        ]

        model = Post
        validators = []