from django.contrib import admin
from .models import Tutorial, TutorialSeries, TutorialCategory
from tinymce.widgets import TinyMCE 
from django.db import models

class TutorialAdmin(admin.ModelAdmin):
	fieldsets = [
		('Title and Date', {'fields': ['tutorial_title', 'tutorial_published', 'tutorial_website']}),
		('URL', {'fields': ['tutorial_slug']}),
		('Series', {'fields': ['tutorial_series']}),
		('Content', {'fields': ['tutorial_content']},)
	]

	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
	}

admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
admin.site.register(Tutorial, TutorialAdmin)
