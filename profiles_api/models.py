from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings



class UserProfileManager(BaseUserManager):
    """ Manager for user profiles """

    def create_user(self, email, first_name, last_name, password=None):
        """ Creates a new user profile """

        if not email:
            raise ValueError("User must have email address")
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,  first_name, last_name, password):
        """ Create super user details """
        user = self.create_user(email, first_name, last_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database profile table for users in the system """
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]


    def get_full_name(self):
        """ Retrieve full name """
        return f"{self.first_name} {self.last_name}"


    def get_short_name(self):
        """ Retrieve short name """
        return self.last_name


    def __str__(self):
        """ Retrieve String Representation of the user profile """
        return self.email



class ProfileFeeds(models.Model):
    """ Profile Feeds Table """

    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """ Return status text of the object """
        return self.status_text

