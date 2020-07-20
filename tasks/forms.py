from django import forms
from django.forms import ModelForm

from .models import *

#creating model form
class TaskForm(forms.ModelForm):
	title = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Add new task...'}))

	class Meta:
		model = Task
		#allowing all field value
		fields = '__all__'