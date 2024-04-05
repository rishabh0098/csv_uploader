from django.db import models

# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=255)
    Class = models.CharField(max_length=255)
    School = models.CharField(max_length=255)
    State = models.CharField(max_length=255)
    def __str__(self):
        return ','.join(self.Name, self.Class, self.School, self.State)

