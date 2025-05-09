from rest_framework import serializers
from .models import Post
from likes.models import Like


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    liked_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        """
        Validate the image field to ensure it is not too:
        - large (2MB)
        - wide (4096px)
        - tall (4096px)
        """
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError("Image size cannot exceed 2MB!")
        if value.image.width > 4096:
            raise serializers.ValidationError(
                "Image width cannot exceed 4096px!"
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                "Image height cannot exceed 4096px!"
            )

        return value

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_liked_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            liked = Like.objects.filter(owner=user, post=obj).first()
            return liked.id if liked else None
        return None

    class Meta:
        model = Post
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "created_at",
            "updated_at",
            "title",
            "content",
            "image",
            "image_filter_choices",
            "liked_id",
            "comments_count",
            "likes_count",
        ]
