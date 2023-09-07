from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class UsernameBackend(ModelBackend):
	def check_user_exists(self, username, password):
		CustomUserModel = get_user_model()
		try:
			return CustomUserModel.objects.get(username=username)
		except CustomUserModel.DoesNotExists:
			return None

	def authenticate(self, request, username, password, **kwargs):
		user = self.check_user_exists(username, password)
		if user:
			if user.check_password(password):
				return user
			return 'Wrong Password!'
		return None

	def get_user(self, username):
		return self.check_user_exists