from channels import Group
from channels.sessions import channel_session
from channels.auth import channel_session_user_from_http, channel_session_user

from .models import Notification


@channel_session_user_from_http
def ws_connect(message):
    subscribed_question_list = message.user.subscribed.all() # all question subscribed by current user
    # add user to all channel Groups for his subscribed questions
    for question in subscribed_question_list:
        Group("question_id_{}".format(question.id)).add(message.reply_channel)

    message.reply_channel.send({"accept": True})



@channel_session_user
def ws_disconnect(message):
    subscribed_question_list = message.user.subscribed.all() # all question subscribed by current user
    # remove user from all channel Groups for his subscribed questions
    for question in subscribed_question_list:
        Group("question_id_{}".format(question.id)).discard(message.reply_channel)

