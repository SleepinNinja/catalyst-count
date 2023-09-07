from django.forms import ModelForm
from .models import File


class UploadForm(ModelForm):
	class Meta:
		model = File
		fields = ('file',)