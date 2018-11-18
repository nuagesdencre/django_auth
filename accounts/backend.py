from django.contrib.auth.models import User

class EmailAuth:
    """
    Authenticate using email and password check
    """
    def authenticate(self, username=None, password=None):
        """
        Get an instance of 'User' based off the email and verify the password
        """
        
        try:
            user = User.objects.get(email=username)
            
            if user.check_password(password):
                
                if user.check_password(password):
                    return user
                return None
        except User.DoesNotExist:
                return None
                
    def get_user(self, user_id):
        """
        Used by the Django authentication system to retrieve user details
        """
        try:
            user = User.objects.get(pk=user_id)
            
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None