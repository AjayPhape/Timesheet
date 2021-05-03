from django.contrib import admin
from .models import Project, Task, TaskLine


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


class TaskLineAdminLine(admin.TabularInline):
    ordering = ('-create_date',)
    model = TaskLine
    extra = 0
    readonly_fields = ('create_date', 'write_date')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'create_date', 'write_date')
    inlines = (TaskLineAdminLine, )
    list_filter = ('project', 'create_date', 'write_date')


@admin.register(TaskLine)
class TaskLineAdmin(admin.ModelAdmin):
    list_display = ('task', 'description', 'create_date', 'write_date')
    readonly_fields = ('create_date', )
    list_select_related = ('task', )

