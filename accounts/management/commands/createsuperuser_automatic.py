import os

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'create super user automatically getting password from\
            environmant variable'

    def handle(self, *args, **options):
        user = os.getenv('USERNAME')
        email = os.getenv('EMAIL')
        password = os.getenv('PASSWORD')

        try:
            User.objects.create_superuser(user, email, password)
            self.stdout.write('created user {}'.format(user))
        except Exception as e:
            self.stdout.write('user not created')
            self.stdout.write('{}'.format(e))