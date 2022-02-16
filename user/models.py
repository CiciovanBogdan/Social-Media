from django.contrib.auth.models import User
from django.db import models


class ExtendUser(User):
    age = models.IntegerField(null=False)
    address = models.CharField(max_length=255)

    def __str__(self):
        return str(self.address)
