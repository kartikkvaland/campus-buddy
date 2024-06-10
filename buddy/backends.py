# backends.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

class EmailAuthBackend(BaseBackend):
    def get_user_by_email(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
