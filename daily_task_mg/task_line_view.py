from django.http import request, HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.core.serializers.json import DjangoJSONEncoder

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from datetime import datetime
import json


from .models import TaskLine
from .forms import TaskForm, TaskLineForm


class TaskLineView(APIView):
	permission_classes = (AllowAny, )

	def get(self, request):
		task_id = request.GET.get('task_id')
		data = TaskLine.objects.filter(task_id=task_id).order_by('work_date').values_list('id', 'name', 'consumed_hours', 'work_date')
		print(request.GET, task_id)
		# if request.query_params:c
		# 	lines = TaskLine.objects.all() \
		# 		.filter(name__contains=request.GET.get('name')) \
		# 		.filter(consumed_hours=request.GET.get('consumed_hours')) \
		# 		.order_by('work_date')
		# data = serializers.serialize('json', data)
		# print(data)
		data = json.dumps({"data":list(data)}, cls=DjangoJSONEncoder)
		return HttpResponse(data, status=201)

	def post(self, request):
		print(request.data.get('task_id'))
		line_obj = TaskLine.objects.create(
			name=request.data.get('name'),
			consumed_hours=request.data.get('consumed_hours'),
			write_date=timezone.now(),
			task_id=request.data.get('task_id'),
			work_date=datetime.strptime(request.data.get('work_date'), "%Y-%m-%d"),
		)
		line_obj.save()
		return HttpResponse(json.dumps(line_obj.id), status=201)

	def put(self, request):
		rec_id = request.data.get('rec_id')
		line_obj = TaskLine.objects.filter(pk=rec_id)
		line_obj.update(
			name=request.data.get('name'),
			consumed_hours=request.data.get('consumed_hours'),
			write_date=timezone.now(),
			work_date=datetime.strptime(request.data.get('work_date'), "%Y-%m-%d"),
			)
		return HttpResponse(status=200)

	def delete(self, request):
		rec_id = request.data.get('rec_id')
		print(rec_id)
		line_obj = TaskLine.objects.get(pk=rec_id)
		line_obj.delete()
		return HttpResponse(status=200)


def view_taskline(request, task_id=None):
	task_line_form = TaskLineForm()
	return render(request, 'task_line.html', {'task_line_form': task_line_form, 'task_id':task_id})