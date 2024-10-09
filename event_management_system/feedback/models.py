from django.db import models

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    user_class = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Rating 1-5
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.semester}'
