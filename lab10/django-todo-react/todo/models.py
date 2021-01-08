from django.db import models
import datetime
# Create your models here.

now = datetime.datetime.now();
formatNow = now.strftime("%d/%m/%Y %H:%M:%S");


# add this
class Todo(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  completed = models.BooleanField(default=False)
  addTime = models.DateField()
  def _str_(self):
    return self.title