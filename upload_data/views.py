from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View, TemplateView
from django.http import JsonResponse
from .models import File
from .forms import UploadForm
from .tasks import upload_to_db
from django.conf import settings
import os



class UploadDataView(LoginRequiredMixin, View):
	def get(self, request):
		form = UploadForm()
		return render(request, 'upload_data.html', context={'form':form})

	def post(self, request):
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			csv_file = form.save()
			print(os.path.join(settings.MEDIA_ROOT, csv_file.file.name))
			file = form.cleaned_data.get('file')
			task = upload_to_db.delay(os.path.join(settings.MEDIA_ROOT, csv_file.file.name))
			return JsonResponse({'data':'Data uploaded', 'task': task.id})
		else:
			return JsonResponse({'data':'Something went wrong!!'})