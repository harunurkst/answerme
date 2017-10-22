from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required
def mark_as_read(request, notification_id):
    request.user.profile.mark_as_read(notification_id)
    return redirect(request.META['HTTP_REFERER'])  # redirect to same url (where form was submitted )

@login_required
def mark_as_unread(request, notification_id):
    request.user.profile.mark_as_unread(notification_id)
    return redirect(request.META['HTTP_REFERER'])  # redirect to same url (where form was submitted )
