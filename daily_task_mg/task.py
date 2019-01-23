from django.http import request, HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.core.serializers.json import DjangoJSONEncoder

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from datetime import datetime
import json


from .models import Task
from .forms import TaskForm, TaskLineForm


class TaskView(APIView):
	permission_classes = (AllowAny, )

	def get(self, request):
		task_id = request.query_params.get('project_id')
		data = Task.objects.all().order_by('create_date').values_list('id', 'name')
		print(request.GET, task_id)
		# if request.query_params:c
		# 	lines = Task.objects.all() \
		# 		.filter(name__contains=request.GET.get('name')) \
		# 		.filter(consumed_hours=request.GET.get('consumed_hours')) \
		# 		.order_by('work_date')
		# data = serializers.serialize('json', data)
		# print(data)
		data = json.dumps({"data":list(data)}, cls=DjangoJSONEncoder)
		return HttpResponse(data, status=201)

	def post(self, request):
		line_obj = Task.objects.create(
			name=request.data.get('name'),
			write_date=timezone.now(),
		)
		line_obj.save()
		return HttpResponse(json.dumps(line_obj.id), status=201)

	def put(self, request):
		rec_id = request.data.get('rec_id')
		line_obj = Task.objects.filter(pk=rec_id)
		line_obj.update(
			name=request.data.get('name'),
			write_date=timezone.now(),
			)
		return HttpResponse(status=200)

	def delete(self, request):
		rec_id = request.data.get('rec_id')
		line_obj = Task.objects.get(pk=rec_id)
		line_obj.delete()
		return HttpResponse(status=200)


def view_task(request, project_id=None):
	task_form = TaskForm()
	return render(request, 'task.html')