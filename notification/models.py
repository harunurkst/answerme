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

    # def mark_as_read(self, user_id):
    #     subscribers_id_list = self.get_subscribers_ids()
    #     if user_id in subscribers_id_list:
    #         subscribers_id_list.remove(user_id)
    #
    #     # remove notification from database
    #     # if there is no subscriber for notification
    #     if len(subscribers_id_list) < 1:
    #         self.delete()
    #     else:
    #         # save subscriber list if there is any subscriber
    #         self.subscribers_ids = ','+str(subscribers_id_list)
    #         self.save()
    #
    #     return 'marked as read'


    def __str__(self):
        return self.text