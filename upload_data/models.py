from django.db import models
import uuid

class File(models.Model):
	uuid = models.UUIDField(default=uuid.uuid4)
	file = models.FileField()


class CompanyModel(models.Model):
	uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
	name = models.CharField(max_length=100)
	domain = models.URLField()
	year_founded = models.PositiveSmallIntegerField(blank=True, null=True)
	industry = models.CharField(max_length=250)
	size_range = models.CharField(max_length=100)
	locality = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	linkedin_url = models.URLField()
	current_employee_estimate = models.PositiveIntegerField()
	total_employee_estimate = models.PositiveIntegerField()

	def save(self, *args, **kwargs):
		if self.year_founded.strip():
			self.year_founded = int(float(self.year_founded))
		else:
			self.year_founded = None
		super(CompanyModel, self).save(*args, **kwargs)