from rest_framework import serializers
from.models import HistorialChip,Chip,Bovinos,Clientes,Fincas,Veredas,Municipio,Departamento

class HistorialChipSerializer(serializers.ModelSerializer):

    class Meta:
        model = HistorialChip
        fields = ['latitud','longitud','fecha','id_chip']


class ChipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chip
        fields = ['codigo','Estado','Coordenadas']

class BovinosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bovinos
        fields = ['Raza','Genero','Color','Sexo','chip','id_finca','id_cliente']

class ClientesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clientes
        fields = ['nombre','apellido','documento','direccion','telefono']

class FincasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fincas
        fields = ['finca','indicaciones','id_vereda']

class VeredasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Veredas
        fields = ['vereda','indicaciones','id_municipio']

class MunicipioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Municipio
        fields = ['municipio','id_departamento']

class DepartamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departamento
        fields = ['departamento']      