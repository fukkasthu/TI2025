from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre_completo = models.CharField(max_length=255)
    correo_electronico = models.EmailField()
    numeros_telefonicos = models.CharField(max_length=255)  # puedes usar un JSONField para varios
    direccion_fisica = models.TextField()
    fecha_nacimiento = models.DateField()
    notas_adicionales = models.TextField(blank=True, null=True)
    eliminado = models.BooleanField(default=False)  # Para el "borrado lógico"

    def __str__(self):
        return self.nombre_completo

