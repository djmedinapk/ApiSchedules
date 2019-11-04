from ..models.Asignation import Asignation
from rest_framework import serializers
from api.models.Classroom import Classroom
from api.models.Classes import Classes
from api.serializers.ClassroomSerializer import ClassroomSerializer
from api.serializers.ClassesSerializer import ClassesSerializer

class AsignationSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:classroom-detail")
    # classroom_fk = serializers.PrimaryKeyRelatedField(queryset=Classroom.objects.all())
    # classes_fk = serializers.PrimaryKeyRelatedField(queryset=Classes.objects.all())
    classroom_fk = ClassroomSerializer()
    classes_fk = ClassesSerializer()
    class Meta:
        model = Asignation
        #fields = '__all__'
        fields = ('id','url','asignation_pk','asignation_start','asignation_end','asignation_day','classroom_fk','classes_fk')