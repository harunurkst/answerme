from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .models import Notification


@login_required
def new_notifications(request):
    # all notifications for current user
    all_notifications = Notification.objects.filter(
        question__subscribers__id=request.user.pk)

    # filter unread notification from all notification
    new_notifications = all_notifications.exclude(
        id__in=request.user.profile.get_read_notifications_id())

    context = {'new_notifications': new_notifications}
    return render(request, 'notification/new_notifications.html', context)


@login_required
def mark_as_read(request, notification_id):
    request.user.profile.mark_as_read(notification_id)
    return redirect(request.META['HTTP_REFERER'])  # redirect to same url (where form was submitted )

@login_required
def mark_as_unread(request, notification_id):
    request.user.profile.mark_as_unread(notification_id)
    return redirect(request.META['HTTP_REFERER'])  # redirect to same url (where form was submitted )
