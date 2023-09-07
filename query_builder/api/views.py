from rest_framework.views import APIView
from rest_framework.response import Response
from upload_data.models import CompanyModel
from rest_framework import status
from .serializers import FilterCompanyDataSerializer
import json

class ListCompanyDataView(APIView):
	def get(self, request):
		bytes_literal = request.body

		if len(bytes_literal.decode('utf-8')) == 0:
			return Response({
				'error': 'Please provide filters for querying data',
			},
			status=status.HTTP_400_BAD_REQUEST
		)

		filters = json.loads(request.body)
		queryset = CompanyModel.objects.all()

		year_founded = filters.get('year_founded')

		if year_founded:
			queryset = queryset.filter(year_founded=int(year_founded))

		city, state = filters.get('city'), filters.get('state')

		if city:
			queryset = queryset.filter(locality__icontains=city.lower())
		if state:
			queryset = queryset.filter(locality__icontains=state.lower())

		filters = {
			key:value.lower() for key,value in
			filters.items() if key not in ['year_founded', 'city', 'state']
		}
		queryset = queryset.filter(**filters)
		serializer = FilterCompanyDataSerializer(queryset, many=True)
		return Response({
				'total result found': len(queryset),
				'result': serializer.data
			},
			status=status.HTTP_200_OK
		)
