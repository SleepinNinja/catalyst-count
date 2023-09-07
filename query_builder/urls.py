from django.urls import path
from .views import QueryBuilderView, ShowQueryResultView

app_name = 'query_builder'

urlpatterns = [
	path('', QueryBuilderView.as_view(), name='query_builder'),
	path('query_result', ShowQueryResultView.as_view(), name='query_result')
]