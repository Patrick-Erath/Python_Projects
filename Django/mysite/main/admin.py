from django.contrib import admin
from .models import Tutorial
from tinymce.widgets import TinyMCE 
from django.db import models

class TutorialAdmin(admin.ModelAdmin):
	fieldsets = [
		('THE TITLE AND THE DATE', {'fields': ['tutorial_title', 'tutorial_published']}),
		('CoNtEnT', {'fields': ['tutorial_content']})
	]

	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
	}

	'''fields = ['tutorial_title',
			  'tutorial_published',
			  'tutorial_content']'''



admin.site.register(Tutorial, TutorialAdmin)

# Register your models here.
