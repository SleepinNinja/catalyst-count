from celery.decorators import task
from .models import CompanyModel
from catalyst_count.redis import redis
import csv

@task(name='upload_to_db')
def upload_to_db(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)

            data_fields = [
                'name', 'domain', 'year_founded','industry',
                'size_range','locality','country', 'linkedin_url',
                'current_employee_estimate', 'total_employee_estimate'
            ]

            for row in reader:
                company_data = {data_fields[i]: row[i + 1] for i in range(len(data_fields))}

                if len(company_data.get('locality').strip()) > 0:
                    location_info = company_data.get('locality').split(',')
                    city, state = location_info[0].strip(), location_info[1].strip()
                    if city:
                        redis.sadd('city', city)
                    if state:
                        redis.sadd('state', state)

                if len(company_data.get('industry').strip()) > 0:
                    redis.sadd('industry', company_data.get('industry'))

                if len(company_data.get('country').strip()) > 0:
                    redis.sadd('country', company_data.get('country'))

                if len(company_data.get('year_founded').strip()) > 0:
                    redis.sadd('year_founded', int(float(str(company_data.get('year_founded')))))

                company = CompanyModel(**company_data)
                company.save()

        return f"Successfully imported data from {file_path}"

    except Exception as e:
        return f"Failed to import data: {str(e)}"
