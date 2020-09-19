from django.db import models
import socket

# Create your models here.
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)


class RouterDetails(models.Model):
    Sapid = models.CharField(max_length=18)
    Host_name = models.CharField(max_length=14)
    Loop_back = models.CharField(max_length=20, default=ip_address)
    Mac_address = models.CharField(max_length=14)
    delete_flag = models.IntegerField(max_length=1, default=0)

    def __str__(self):
        return self.Host_name
