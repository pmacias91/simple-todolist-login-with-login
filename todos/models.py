from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todos(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="Title")
    notes = models.TextField('Notes', blank=True, null=True)
    created_at = models.DateTimeField('Created', auto_now_add=True)
    update_at = models.DateTimeField('Updated', auto_now=True)
    isCompleted = models.BooleanField('Completed',default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"