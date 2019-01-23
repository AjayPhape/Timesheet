from django.http import request, HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .models import TaskLine

from datetime import datetime
import json

class TaskLineView(APIView):
	permission_classes = (AllowAny, )

	def get(self, request):
		task_id = request.query_params.get('task_id')
		data = TaskLine.objects.all().order_by('work_date').values_list('id', 'name', 'consumed_hours', 'consumed_hours')
		# import pdb;pdb.set_trace()
		print(request.GET, task_id)
		# if request.query_params:c
		# 	lines = TaskLine.objects.all() \
		# 		.filter(name__contains=request.GET.get('name')) \
		# 		.filter(consumed_hours=request.GET.get('consumed_hours')) \
		# 		.order_by('work_date')
		# data = serializers.serialize('json', data)
		# print(data)
		data = json.dumps({"data":list(data)})
		return HttpResponse(data, status=201)

	def post(self, request):
		# print(datetime.strptime(request.data.get('work_date').replace(".000Z", ""), "%Y-%m-%dT%H:%M:%S"))
		line_obj = TaskLine.objects.create(
			name=request.data.get('name'),
			consumed_hours=request.data.get('consumed_hours'),
			write_date=timezone.now(),
			# work_date=datetime.strptime(request.data.get('work_date').replace(".000Z", ""), "%Y-%m-%dT%H:%M:%S"),
		)
		line_obj.save()
		return HttpResponse(json.dumps(line_obj.id), status=201)

	def put(self, request):
		rec_id = request.data.get('rec_id')
		print(rec_id)
		line_obj = TaskLine.objects.filter(pk=rec_id)
		print(request.data.get('work_date'))
		line_obj.update(
			name=request.data.get('name'),
			consumed_hours=request.data.get('consumed_hours'),
			write_date=timezone.now(),
			# work_date=datetime.strptime(request.data.get('work_date').replace(".000Z", ""), "%Y-%m-%dT%H:%M:%S")
			)
		return HttpResponse(status=200)

	def delete(self, request):
		rec_id = request.data.get('rec_id')
		print(rec_id)
		line_obj = TaskLine.objects.get(pk=rec_id)
		line_obj.delete()
		return HttpResponse(status=200)


def view_timeline(request, project_id=None, task_id=None):

	return render(request, 'index.html')