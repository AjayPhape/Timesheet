from django.contrib import admin

from server_management.models import ServerReadInfo, ServerInfo


@admin.register(ServerInfo)
class ServerInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'ssh_ip', 'directory', 'env_directory', 'supervisor_env', 'supervisor_command')


@admin.register(ServerReadInfo)
class ServerReadInfoAdmin(admin.ModelAdmin):
    list_display = ServerInfoAdmin.list_display

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False