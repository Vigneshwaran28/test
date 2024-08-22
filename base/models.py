from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=120)
    english = models.IntegerField()
    tamil = models.IntegerField()
    maths = models.IntegerField()

    def total(self):
        return self.english + self.tamil + self.maths
    

    def average(self):
        return int(self.total() / 3 )
    

    def __str__(self):
        return self.name
    