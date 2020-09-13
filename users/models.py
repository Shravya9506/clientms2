from django.contrib.auth.models import AbstractUser
from django.db import models


# Extends the AbstractUser which has basic user information
class CustomUser(AbstractUser):
    department = models.CharField(max_length=50, default=' ', null=True, blank=True)
    employee_cell_phone = models.CharField(max_length=50, default=' ', null=True, blank=True)
