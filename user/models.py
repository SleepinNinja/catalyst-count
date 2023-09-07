from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .model_manager import CustomUserModelManager
import uuid

class CustomUser(AbstractBaseUser, PermissionsMixin):
	uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
	username = models.CharField(max_length=20, unique=True)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20, blank=True, null=True)
	email = models.EmailField(unique=True, blank=True, null=True)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []

	objects = CustomUserModelManager()

	def __str__(self):
		return f'Name: {self.first_name.title()} {self.last_name.title() if self.last_name else ""} Email: {self.email}'

	def get_full_name(self):
		return self.first_name.title() + ' ' +self.last_name.title() if self.last_name else ''