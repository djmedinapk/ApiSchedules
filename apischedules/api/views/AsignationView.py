from rest_framework import viewsets
from api.models.Asignation import Asignation
from api.serializers.AsignationSerializer import AsignationSerializer

class AsignationView(viewsets.ModelViewSet):
    queryset = Asignation.objects.all()
    serializer_class = AsignationSerializer
