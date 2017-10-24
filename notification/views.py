from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Notification


@login_required
def notifications(request):
    # retrieve all new notifications of current user
    new_notification = Notification.objects.filter(
        subscribers_ids__contains=request.user.id)

    context = {'notifications': new_notification}
    return render(request, 'notification/notifications.html', context)


@login_required
def mark_as_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)
    # related question of this notification
    # for redirect to question detail
    question = notification.question
    notification.mark_as_read(user_id=request.user.id)

    # redirect to related question detail
    return redirect(question.get_absolute_url())

@login_required
def mark_all_as_read(request, notification_id):
    # redirect to previous url (where form was submitted )
    return redirect(request.META['HTTP_REFERER'])
