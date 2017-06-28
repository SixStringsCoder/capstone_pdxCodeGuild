from django.db import models
from django.contrib.auth.models import AbstractUser


def profile_upload_handler(instance, filename) -> str:
    """
    Handler to provide link to User profile image

    """
    username = instance.owner.username
    return f"{username}/{instance.name}/{filename}"



class User(AbstractUser):
    """
    User accounts to make collections

    Users within the Django authentication system are represented by this
    model.

    Username, password and email are required. Other fields are optional.

    """
    nickname = models.CharField(max_length=256)
    image = models.ImageField(upload_to=profile_upload_handler),


    REQUIRED_FIELDS = ['nickname', 'email']