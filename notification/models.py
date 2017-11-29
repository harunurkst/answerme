from django.db import models

from question.models import Question
from answer.models import Answer


class Notification(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='notifications')
    text = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    subscribers_ids = models.TextField(default='', help_text="comma sepereted integer, subscribers id's")
    unread_subscribers_ids = models.TextField(default='', help_text="comma sepereted integer, id's of unread subscribers")


    def get_subscribers_ids(self):
        return list(map(int, self.subscribers_ids.split(',')))

    def get_unread_subscribers_ids(self):
        return list(map(int, self.unread_subscribers_ids.split(',')))

    def mark_as_read(self, subscriber_id):
        unread_subscirbers = self.get_unread_subscribers_ids()
        if subscriber_id in unread_subscirbers:
            unread_subscirbers.remove(subscriber_id)

        self.unread_subscribers_ids = ','.join(map(str, unread_subscirbers))
        self.save()
        return 'marked as read'


    def mark_as_unread(self, subscriber_id):
        unread_subscirbers = self.get_unread_subscribers_ids()
        if not subscriber_id in unread_subscirbers:
            unread_subscirbers.append(subscriber_id)

        self.unread_subscribers_ids = ','.join(map(str, unread_subscirbers))
        self.save()
        return 'marked as unread'


    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created']
