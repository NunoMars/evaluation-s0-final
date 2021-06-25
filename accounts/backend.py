from .models import CustomUser


class CustomUserAuth(object):
    def authenticate(self, username=None, password=None):
        """
        User custom Autentification
        """
        try:
            user = CustomUser.objects.get(email=username)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None
