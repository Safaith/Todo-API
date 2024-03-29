from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length =100, blank=False)
    description = models.TextField(max_length=200, blank=True)
    date = models.DateField(blank=False)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title 
