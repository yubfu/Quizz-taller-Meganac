from django.shortcuts import render
from django.views.generic import TemplateView

from .models import HistorialChip,Chip,Bovinos,Clientes,Fincas,Veredas,Municipio,Departamento
from rest_framework import viewsets
from .serializers import HistorialChipSerializer, ChipSerializer, BovinosSerializer, ClientesSerializer, FincasSerializer, VeredasSerializer, MunicipioSerializer, DepartamentoSerializer


#api manual

from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST
)
from rest_framework.response import Response

# Create your views here.

class HistorialChipViewSet(viewsets.ModelViewSet):
    queryset = HistorialChip.objects.all()
    serializer_class = HistorialChipSerializer

class ChipViewSet(viewsets.ModelViewSet):
    queryset = Chip.objects.all()
    serializer_class = ChipSerializer

class BovinosViewSet(viewsets.ModelViewSet):
    queryset = Bovinos.objects.all()
    serializer_class = BovinosSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer

class FincasViewSet(viewsets.ModelViewSet):
    queryset = Fincas.objects.all()
    serializer_class = FincasSerializer

class VeredasViewSet(viewsets.ModelViewSet):
    queryset = Veredas.objects.all()
    serializer_class = VeredasSerializer


class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer




@api_view(['GET'])
def clientesShow(request):
    clientes = Clientes.objects.all()

    result = []

    for i in clientes:
        data = {}
        data['cliente_nombre'] = i.clientes.nombre
        data['cliente_apellido'] = i.clientes.apellido
        data['cliente_documento'] = i.clientes.documento
        data['cliente_direccion'] = i.clientes.direccion
        data['cliente_telefono'] = i.clientes.telefono
        result.append(data)
    return Response({'item':result}, status = HTTP_200_OK)

