"""timesheet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from daily_task_mg import task_line_view, task

urlpatterns = [
    path('task_line', task_line_view.view_taskline, name='task_line'),
    path('task_line/<int:task_id>', task_line_view.view_taskline),
    path('api/task_line/', task_line_view.TaskLineView.as_view()),

    path('task', task.view_task, name='task'),
    path('api/task/', task.TaskView.as_view()),
]

