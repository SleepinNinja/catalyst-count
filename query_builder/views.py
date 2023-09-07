from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from catalyst_count.redis import redis
from upload_data.models import CompanyModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from django.core.exceptions import ValidationError


class QueryBuilderView(TemplateView):
	template_name = 'query_builder.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['industries'] = redis.sort('industry', alpha=True)
		context['year_founded'] = redis.sort('year_founded')
		context['cities'] = redis.sort(name='city', alpha=True)
		context['states'] = redis.sort('state', alpha=True)
		context['countries'] = redis.sort('country', alpha=True)
		return context



class ShowQueryResultView(ListView):
	model = CompanyModel
	template_name = 'show_query_data.html'

	def get_filter_queryset(self, **kwargs):
		have_values = {
			key: value.lower() for key, value in
			self.request.GET.items() if value.strip() != ''
		}

		queryset = CompanyModel.objects.all()

		if len(have_values) == 0:
			return None

		city = self.request.GET.get('city')
		state = self.request.GET.get('state')

		if city:
			queryset = queryset.filter(locality__icontains=city)
			have_values.pop('city')
		if state:
			queryset = queryset.filter(locality__icontains=state)
			have_values.pop('state')

		if have_values.get('year_founded'):
			have_values['year_founded'] = int(have_values['year_founded'])

		queryset = queryset.filter(**have_values)
		return queryset

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		queryset = self.get_filter_queryset()
		context['result'] = self.get_filter_queryset()
		return context