from django.urls import path
from .views import UploadDataView

app_name = 'upload_data'


urlpatterns = [
	path('', UploadDataView.as_view(), name='upload_data'),
]