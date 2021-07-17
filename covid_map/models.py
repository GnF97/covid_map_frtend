from django.db import models

# Create your models here.
class Patient(models.Model):
    idp = models.IntegerField(max_length=4)
    startD = models.DateTimeField()
    endD = models.DateTimeField()

    def __str__(self):
        return f"{self.idp} tests positive at {self.startD}"

class County(models.Model):
    idc = models.CharField(max_length=4)
    # patient_count = models.ForeignKey(Patient, max_length=10,on_delete=models.CASCADE, related_name="level")
    patient_count = models.IntegerField(max_length=10)

    def __str__(self):
        return f"{self.idc}'s today total count is {self.patient_count}"


