from django.db import models

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=50)
    esal = models.IntegerField()
    eaddr = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.ename} (ID: {self.eno})"
