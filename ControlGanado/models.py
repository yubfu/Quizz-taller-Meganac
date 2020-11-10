from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Clientes(models.Model):
    nombre = models.CharField(max_length= 102, blank=False)
    apellido = models.CharField(max_length= 102, blank=False)
    documento = models.CharField(max_length= 102, unique=True)
    direccion=models.CharField(max_length=100, blank=False)
    telefono= models.CharField(max_length=30, blank=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural= _('Clientes')

class Departamento(models.Model):
    departamento = models.CharField(max_length= 100, blank=False)

    def __str__(self):
        return str(self.departamento) 
    #el return se encuentra convirtiendo a string porque originalmente mostraba el id, pero para guia y mejor interpretacion de las tablas en el admin  deje el nombre
    class Meta:
        verbose_name_plural= _('Departamento')


class Municipio(models.Model):
    municipio = models.CharField(max_length= 100, blank=False)
    id_departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.municipio)

    class Meta:
        verbose_name_plural= _('Municipio')

class Veredas(models.Model):
    vereda = models.CharField(max_length= 102, blank=False)
    indicaciones = models.TextField(blank=False)
    id_municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.vereda)

    class Meta:
        verbose_name_plural= _('Veredas')

class Fincas(models.Model):
    finca = models.CharField(max_length= 102, blank=False)
    indicaciones = models.TextField(blank=False)
    id_vereda = models.ForeignKey(Veredas, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.finca)

    class Meta:
        verbose_name_plural= _('Fincas')



class Chip(models.Model):
    codigo = models.IntegerField(blank=False)
    Estado = models.CharField(max_length= 20, blank=False)
    Coordenadas = models.CharField(max_length= 20, blank=False)

    def __str__(self):
        return str(self.codigo)

    class Meta:
        verbose_name_plural= _('Chip')




class Bovinos(models.Model):
    Raza = models.CharField(max_length= 100, blank=False)
    Genero = models.CharField(max_length= 50, blank=False)
    Color = models.CharField(max_length= 50, blank=False)
    Sexo = models.CharField(max_length= 50, blank=False)
    chip = models.OneToOneField(Chip, on_delete=models.CASCADE, null=False, blank=False)
    id_finca = models.ForeignKey(Fincas, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
        
    def __str__(self):
        return str(self.id) 

    class Meta:
        verbose_name_plural= _('Bovinos')


class HistorialChip(models.Model):
    latitud = models.CharField(max_length= 50, blank=False)
    longitud = models.CharField(max_length= 20, blank=False)
    fecha = models.DateTimeField(auto_now_add=True)
    id_chip = models.ForeignKey(Chip, on_delete=models.CASCADE)

    
    def __str__(self):
        return str(self.id) 

    class Meta:
        verbose_name_plural= _('Historial Chip')















