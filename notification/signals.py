from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from answer.models import Answer
from question.models import Question
from .models import Notification


@receiver(post_save, sender=Answer)
def create_notification(sender, instance, created, **kwargs):
    if created:
        notification = Notification()
        notification.question = instance.question
        notification.text = 'new answer submitted on "{}" at: {}'.format(instance.question, instance.created)
        notification.save()
