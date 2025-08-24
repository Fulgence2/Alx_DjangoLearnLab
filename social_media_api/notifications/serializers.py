from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()      # shows actor username
    recipient = serializers.StringRelatedField()  # shows recipient username
    target_repr = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ["id", "recipient", "actor", "verb", "target_repr", "timestamp", "read"]

    def get_target_repr(self, obj):
        if obj.target:
            return str(obj.target)  # e.g., "Post by Alice at 2025-08-24"
        return None
