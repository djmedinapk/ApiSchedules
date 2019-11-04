from rest_framework import viewsets
from api.models.Classroom import Classroom
from api.serializers.ClassroomSerializer import ClassroomSerializer

class ClassroomView(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
