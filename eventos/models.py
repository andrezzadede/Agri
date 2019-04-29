from django.db import models

class Estado(models.Model):
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.estado


class Evento(models.Model):
    data = models.DateField()
    cidade = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, null=True, blank=True, on_delete=models.PROTECT)


    def __str__(self):
        return self.cidade