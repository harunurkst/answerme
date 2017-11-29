from django.db.models.signals import post_save
from django.dispatch import receiver

from channels import Group

from answer.models import Answer
from .models import Notification


# create notification after created any answer
@receiver(post_save, sender=Answer)
def create_notification(sender, instance, created, **kwargs):
    if created:
        # retrieve all subscriber of question for this answer
        subsriber_list_of_question_for_these_answer = instance.question.subscribers.all()

        if subsriber_list_of_question_for_these_answer.count(): # if any subscriber, then create notification
            # list of subscribers id
            subscriber_id_list = []
            for subscriber in subsriber_list_of_question_for_these_answer:
                subscriber_id_list.append(str(subscriber.id))

            # creating new notification
            notification = Notification()
            notification.question = instance.question
            notification.text = '"{}" answered on "{}".'.format(instance.text, instance.question)
            # insert subscriber_id_list in notification.subscribers_ids as comma separated id list
            notification.subscribers_ids = ','.join(subscriber_id_list)
            # insert all subscribers into unread subscribers list
            notification.unread_subscribers_ids = notification.subscribers_ids[:] # copy list
            notification.save() # save notification

            # send notification alert on websocket
            # by channel Group
            Group("question_id_{}".format(notification.question.id)).send({
                "text": notification.text,
            })
