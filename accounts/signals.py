from .models import Profile
from django.dispatch import receiver
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount
from django.db.models.signals import post_save,pre_save

"""
@receiver(post_save, sender=SocialAccount)
def social_login_profilepic(instance, **kwargs):
    preferred_profile_size_pixels = 256
    request_user_id =instance.user_id
    user_intance = User.objects.get(id=request_user_id)
    if instance.provider == 'facebook':
        account_uid = SocialAccount.objects.filter(user_id=request_user_id, provider='facebook')
        UID = account_uid[0].extra_data['id']
        object, create = Profile.objects.get_or_create(user_id=request_user_id)
        picture_url = "http://graph.facebook.com/{0}/picture?width={1}&height={1}".format(
                    UID, preferred_profile_size_pixels)
        if create:
                object.user = user_intance
                object.profile_pic_url = picture_url
                object.save()
"""