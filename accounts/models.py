from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photo/', blank=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=50, blank=True)
    read_notifications_id = models.TextField(default='0', help_text="comma sepereted integer, read notification id's")

    def get_read_notifications_id(self):
        return list(map(int, self.read_notifications_id.split(',')))

    def mark_as_read(self, notification_id):
        self.read_notifications_id = self.read_notifications_id + ','+str(notification_id)
        self.save()
        return 'marked as read'

    def mark_as_unread(self, notification_id):
        read_notification_id = self.get_read_notifications_id()
        if notification_id in read_notification_id:
            read_notification_id.remove(notification_id)
        self.read_notifications_id = ','.join(map(str, read_notification_id))
        self.save()
        return 'marked as unread'

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

