from django.db import models

class LogEntry(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    user_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.timestamp} - IP: {self.ip_address} - User ID: {self.user_id}"