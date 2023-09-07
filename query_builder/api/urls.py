from django.urls import path
from .views import ListCompanyDataView

app_name = 'query_builder_api'

urlpatterns = [
	path('', ListCompanyDataView.as_view(), name='query_result_api')
]