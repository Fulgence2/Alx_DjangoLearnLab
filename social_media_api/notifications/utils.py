from .models import Notification
from django.contrib.contenttypes.models import ContentType

def create_notification(recipient, actor, verb, target=None):
    return Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        target_ct=ContentType.objects.get_for_model(target) if target else None,
        target_id=target.id if target else None,
    )
