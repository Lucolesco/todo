from django.db import models

# Create your models here.

class Task(models.Model):
    STATUS = [
        (True, "Done"),
        (False, "In-Progress")
    ]

    id = models.BigAutoField(verbose_name="ID", primary_key=True)
    content = models.CharField(verbose_name="CONTENT", null=False,blank=False, max_length=65)
    status = models.BooleanField(verbose_name="STATUS", null=False, blank=False, choices=STATUS, default=False)
    deadline = models.DateField(verbose_name="DEADLINE", null=False, blank=False)

    def __str__(self):
        return "{}".format(self.content)
    
