from django.db import models

class Prenda(models.Model):
    CHOICES=(
        ('S','S'),
        ('M','M'),
        ('L','L'),
        ('XL','XL'),
    )
    talla=models.CharField(max_length=10,choices=CHOICES)
    tela=models.CharField(max_length=50)
    precio=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.talla}-{self.precio}"
# Create your models here.
