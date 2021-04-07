from django.db import models
from datetime import date

# Create your models here.
class SafetyAlertMsg(models.Model):
    title = models.CharField(max_length=300)
    number = models.CharField(max_length=10, null=True)
    sam_date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.title}"

class SafetyAlertMsgImages(models.Model):
    alert_msg = models.ForeignKey(SafetyAlertMsg, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')