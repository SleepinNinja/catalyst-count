from django.contrib.auth.models import BaseUserManager

class CustomUserModelManager(BaseUserManager):
	def create_user(self, username=None, password=None, **kwargs):
		print(username, password, kwargs)
		if not username:
			raise ValueError('Please provide a username!')

		email = kwargs.get('email')
		first_name = kwargs.get('first_name')
		last_name = kwargs.get('last_name')
		user = self.model(
			username=username,
			email=email if email else '',
			first_name=first_name if first_name else '',
			last_name=last_name,
			**kwargs
		)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, username, password, **kwargs):
		kwargs.setdefault('is_staff', True)
		kwargs.setdefault('is_superuser', True)
		kwargs.setdefault('is_active', True)
		return self.create_user(username, password, **kwargs)


