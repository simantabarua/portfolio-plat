from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def _create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError("Username is required")
        if not email:
            raise ValueError("Email is required.")
        
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            # first_name=first_name,
            # last_name=last_name,
            **extra_fields
        )
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, **extra_fields)
    
    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)  # Ensure user is active
        return self._create_user(username, email, password, **extra_fields)
