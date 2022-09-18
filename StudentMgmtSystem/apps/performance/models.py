from django.db import models

class Reports(models.Model):
    student=models.ForeignKey('registration.Student',on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    tasks=models.IntegerField()
    quizz=models.IntegerField()
    LinkdIn=models.IntegerField()
    presentation=models.IntegerField()

# Create your models here.
