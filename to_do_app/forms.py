from django import forms
from .models import Work

class WorkForm(forms.ModelForm):
	class Meta:
		model = Work
		fields = ["work", "due_time", "priority", "completed","created_time"]