from django.db import models

class Userdata(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    passwordd=models.CharField(max_length=100)

    class Meta:
        db_table='lee'
    


