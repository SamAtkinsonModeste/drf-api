from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    Adds three extra fields when returning a list of Like instances
    """

    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Like
        fields = ["id", "owner", "post", "created_at"]
