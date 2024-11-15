from django.db import models

class Comuna(models.Model):
    id= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=35)
    def __str__(self):
        return str(self.id)+" "+self.nombre
