from django.db import models

# Create your models here.

class Todo(models.Model):
    PRIORITY = (  # normalde list içinde tuple. ama böyle de olur.
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low'),
    )
    task = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    priority = models.SmallIntegerField(choices=PRIORITY, default=3)
    is_done = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.task