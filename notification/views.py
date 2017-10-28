from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Notification


@login_required
def all_notifications(request):
    # retrieve all notifications of current user
    all_notifications = Notification.objects.filter(
        question__subscribers__id=request.user.id
    )

    context = {'notifications': all_notifications}
    return render(request, 'notification/notifications.html', context)

@login_required
def unread_notifications(request):
    # retrieve all notifications of current user
    all_notifications = Notification.objects.filter(
        question__subscribers__id=request.user.id
    )
    # filter unread notification from all notifications
    unread_notifications = all_notifications.filter(is_unread=True)

    context = {'notifications': unread_notifications}
    return render(request, 'notification/notifications.html', context)

@login_required
def read_notification(request, notification_id):
    # get expected notification object
    notification = get_object_or_404(Notification, id=notification_id)
    # mark notification as read
    notification.mark_as_read()
    # get related question of this notification
    # for redirect to question detail
    question = notification.question

    # redirect to related question detail
    return redirect(question.get_absolute_url())

@login_required
def mark_as_read(request, notification_id):
    # get expected notification object
    notification = get_object_or_404(Notification, id=notification_id)
    # mark notification as read
    notification.mark_as_read()

    # redirect to previous url (where mark as read button was submitted )
    return redirect(request.META['HTTP_REFERER'])


@login_required
def mark_as_unread(request, notification_id):
    # get expected notification object
    notification = get_object_or_404(Notification, id=notification_id)
    # mark notification as unread
    notification.mark_as_unread()

    # redirect to previous url (where mark as unread button was submitted )
    return redirect(request.META['HTTP_REFERER'])


@login_required
def mark_all_as_read(request):
    # retrieve all notifications of current user
    all_notifications = Notification.objects.filter(
        question__subscribers__id=request.user.id
    )
    # filter unread notification from all notifications
    unread_notifications = all_notifications.filter(is_unread=True)

    # mark all unread notifications as read
    for notification in unread_notifications:
        notification.mark_as_read()

    # redirect to previous url (where mark_all_as_read was submitted )
    return redirect(request.META['HTTP_REFERER'])