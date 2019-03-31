from django.db import models
from datetime import datetime

# Create your models here.
  
# Define Tutorial model (all models will inherit from models.Model)
class Tutorial(models.Model):
	tutorial_title = models.CharField(max_length=200) # Charfield for limiting field
	tutorial_content = models.TextField() # Text field for no limit
	tutorial_published = models.DateTimeField('date published', default=datetime.now) # date&time represented in pythons datetime.datetime instance

	# Overwrite string method
	def __str__(self): 
		return self.tutorial_title