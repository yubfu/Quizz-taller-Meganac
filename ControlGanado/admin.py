from django.contrib import admin

# Register your models here.
from.models import HistorialChip,Chip,Bovinos,Clientes,Fincas,Veredas,Municipio,Departamento

class ClientesAdmin(admin.ModelAdmin):
    search_fields = ['documento','id']
    list_filter = ['id','documento']
    list_display = ('id','nombre','apellido','documento','direccion','telefono')

class HistorialChipAdmin(admin.ModelAdmin):
    search_fields = ['id','fecha']
    list_filter = ['fecha']
    list_display = ('id','latitud','longitud','fecha','id_chip')

class ChipAdmin(admin.ModelAdmin):
    search_fields = ['id','codigo','Estado']
    list_filter = ['id','codigo','Estado']
    list_display = ('id','codigo','Estado','Coordenadas')


class BovinosAdmin(admin.ModelAdmin):
    search_fields = ['id','Raza','Genero','Sexo','chip']
    list_filter = ['id','Raza','Genero','Sexo','chip']
    list_display = ('id','Raza','Color','Genero','Sexo','chip','id_finca','id_cliente')

class FincasAdmin(admin.ModelAdmin):
    search_fields = ['id','finca','id_vereda']
    list_filter = ['id','finca','id_vereda']
    list_display = ('id','finca','indicaciones','id_vereda')

class VeredasAdmin(admin.ModelAdmin):
    search_fields = ['id','vereda']
    list_filter = ['id','vereda']
    list_display = ('id','vereda','indicaciones','id_municipio')

class MunicipioAdmin(admin.ModelAdmin):
    search_fields = ['id','municipio']
    list_filter = ['id','municipio']
    list_display = ('id','municipio','id_departamento')

class DepatamentoAdmin(admin.ModelAdmin):
    search_fields = ['id','departamento']
    list_filter = ['id','departamento']
    list_display = ('id','departamento')



admin.site.register(HistorialChip, HistorialChipAdmin)
admin.site.register(Chip, ChipAdmin)
admin.site.register(Bovinos, BovinosAdmin)
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Fincas, FincasAdmin)
admin.site.register(Veredas, VeredasAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Departamento, DepatamentoAdmin)