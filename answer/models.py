from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from question.models import Question


class Answer(models.Model):
    user       = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, blank=True)
    question   = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text       = models.TextField()

    created    = models.DateTimeField(auto_now=True)
    updated    = models.DateTimeField(auto_now_add=True)
    upvote     = models.PositiveIntegerField(default=0)
    accepted  = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('question:index', kwargs={'pk':self.question.pk})

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-accepted','upvote', '-created']