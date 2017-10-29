from django.db import models

from question.models import Question
from answer.models import Answer


class Notification(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='notifications')
    text = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    is_unread = models.BooleanField(default=True)
    subscribers_ids = models.TextField(default='', help_text="comma sepereted integer, read subscribers id's")

    def get_subscribers_ids(self):
        return list(map(int, self.subscribers_ids.split(',')))

    def mark_as_read(self):
        self.is_unread = False
        self.save()
        return 'marked as read'

    def mark_as_unread(self):
        self.is_unread = True
        self.save()
        return 'marked as unread'

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created']