from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from datetime import date
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.


class BaseModel(models.Model):
	name = models.CharField(max_length=20)
	description = models.TextField(max_length=2000)
	create_date = models.DateTimeField(default=timezone.now)
	write_date = models.DateTimeField(default=timezone.now)
	create_uid = models.ForeignKey(User, related_name='created%(app_label)s_%(class)s_related', on_delete=models.SET_NULL, null=True)
	write_uid = models.ForeignKey(User, related_name='updated%(app_label)s_%(class)s_related', on_delete=models.SET_NULL,  null=True)

	class Meta:
		abstract = True


class Project(BaseModel):
	def __str__(self):
		return str(self.name)


class Task(BaseModel):
	project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return str(self.name)


class TaskLine(BaseModel):
	task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
	work_date = models.DateField(default=date.today)
	consumed_hours = models.IntegerField(null=True)

	def __str__(self):
		return str(self.name)
