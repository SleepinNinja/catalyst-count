from rest_framework.serializers import ModelSerializer
from rest_framework import exceptions
from upload_data.models import CompanyModel

class FilterCompanyDataSerializer(ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = '__all__'