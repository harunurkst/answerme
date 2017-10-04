from django.db import models

class Question(models.Model):
    qs = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #user = models.CharField(max_length=150)

    def __str__(self):
        return self.qs
