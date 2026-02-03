from django.db import models

class CompanyTool(models.Model):
    tool_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    is_cloud_based = models.BooleanField()

    def __str__(self):
        return self.tool_name