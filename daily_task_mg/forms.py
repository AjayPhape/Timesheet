from django import forms
from .models import Task, TaskLine


class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		exclude = []


class TaskLineForm(forms.ModelForm):
	class Meta:
		model = TaskLine
		exclude = ['create_uid', 'write_uid', 'create_date', 'write_date', 'name', 'description', 'work_date', 'consumed_hours']

	def __init__(self, *args, **kwargs):
		super(TaskLineForm, self).__init__(*args, **kwargs)

		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})