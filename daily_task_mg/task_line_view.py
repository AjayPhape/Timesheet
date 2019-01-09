from django.http import request, HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .models import TaskLine

from datetime import datetime


class TaskLineView(APIView):
	permission_classes = (AllowAny, )

	def get(self, request):
		lines = TaskLine.objects.all().order_by('work_date')
		print(request.GET)
		# if request.query_params:
		# 	lines = TaskLine.objects.all() \
		# 		.filter(name__contains=request.GET.get('name')) \
		# 		.filter(consumed_hours=request.GET.get('consumed_hours')) \
		# 		.order_by('work_date')
		data = serializers.serialize('json', lines)
		return HttpResponse(data, status=201)

	def post(self, request):
		print(datetime.strptime(request.data.get('work_date').replace(".000Z", ""), "%Y-%m-%dT%H:%M:%S"))
		TaskLine.objects.create(
			name=request.data.get('name'),
			consumed_hours=request.data.get('consumed_hours'),
			write_date=timezone.now(),
			work_date=datetime.strptime(request.data.get('work_date').replace(".000Z", ""), "%Y-%m-%dT%H:%M:%S"),
		).save()
		return HttpResponse(status=201)

	def put(self, request, rec_id):
		line_obj = TaskLine.objects.filter(pk=rec_id)
		line_obj.update(name=request.data.get('name'),
						consumed_hours=request.data.get('consumed_hours'),
						write_date=timezone.now(),
						work_date=datetime.strptime(request.data.get('work_date').replace(".000Z", ""), "%Y-%m-%dT%H:%M:%S")
						)
		return HttpResponse(status=200)

	def delete(self, request, rec_id):
		line_obj = TaskLine.objects.get(pk=rec_id)
		line_obj.delete()
		return HttpResponse(status=200)


def view_timeline(request):
	return render(request, 'basic.html')