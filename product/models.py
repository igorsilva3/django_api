from django.db import models

# Create your models here.
class Product(models.Model):
	"""Model definition for Product."""

	id = models.AutoField(primary_key=True)
	name = models.CharField("Name", max_length=60, blank=False)
	value = models.FloatField("Value")
	created_date = models.DateField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)

	class Meta:
		"""Meta definition for Product."""
		verbose_name = 'Product'
		verbose_name_plural = 'Products'

	def __str__(self):
		"""Unicode representation of Product."""
		return self.name