from django.db import models
from datetime import datetime

# Create your models here.
class TutorialCategory(models.Model):
	tutorial_category = models.CharField(max_length=200)
	#tutorial_conte
	category_slug = models.CharField(max_length=200, default=1)

	class Meta:
		# Gives the proper plural name for admin
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.tutorial_category


class TutorialSeries(models.Model):
	tutorial_series = models.CharField(max_length=200)
	tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
	series_summary = models.CharField(max_length=200)

	class Meta:
		# Otherwise we get "Tutorial Series in admin"
		verbose_name_plural = "Series"

	def __str__(self):
		return self.tutorial_series
  
# Define Tutorial model (all models will inherit from models.Model)
class Tutorial(models.Model):
	tutorial_title = models.CharField(max_length=200) # Charfield for limiting field
	tutorial_content = models.TextField() # Text field for no limit
	tutorial_published = models.DateTimeField('date published', default=datetime.now) # date&time represented in pythons datetime.datetime instance
	tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
	tutorial_slug = models.CharField(max_length=200, default=1)
	tutorial_website = models.CharField(max_length=100, default=1)
	# Overwrite string method
	def __str__(self): 
		return self.tutorial_title