from django.contrib.auth.models import User
from django.db import models


class ExtendUser(User):
    profile_picture = models.ImageField(null=True, blank=True, upload_to='profile_picture/')
    age = models.IntegerField(null=False, default='unknown')
    address = models.CharField(max_length=255, default='unknown')

    def __str__(self):
        return str(self.address)
