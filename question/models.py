from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Question(models.Model):
    user       = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, blank=True)
    text       = models.TextField()
    created    = models.DateTimeField(auto_now=True)
    updated    = models.DateTimeField(auto_now_add=True)
    upvote     = models.PositiveIntegerField(default=0)
    is_banned  = models.BooleanField(default=False)
    subscribers= models.ManyToManyField(User, related_name='subscribed', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('question:index', kwargs={'pk':self.pk})

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created', 'upvote']
