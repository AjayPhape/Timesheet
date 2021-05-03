from django.db import models

# Create your models here.
from task_management.models import BaseModel


class ServerInfo(BaseModel):
    name = models.CharField(max_length=10)
    ssh_ip = models.CharField(max_length=70, null=True)
    directory = models.CharField(max_length=200)
    env_directory = models.CharField(max_length=200)
    supervisor_env = models.CharField(max_length=200)
    supervisor_command = models.CharField(max_length=70)

    def __str__(self):
        return str(self.name)


class ServerReadInfo(ServerInfo):
    class Meta:
        proxy = True

    def __str__(self):
        return str(self.name)
