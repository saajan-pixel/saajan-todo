from django.db import models

# Create your models here.
class Task(models.Model):
    id=models.PositiveIntegerField(primary_key=True)
    title=models.CharField(max_length=45)
    description=models.TextField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
