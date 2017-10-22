from django.db import models

from question.models import Question


class Notification(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='notifications')
    text = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'notification: {}! created on: {}.'.format(self.text, self.created)