from ..models.Classroom import Classroom
from rest_framework import serializers

class ClassroomSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:classroom-detail")
    class Meta:
        model = Classroom
        fields = ('id','url','classroom_pk','classroom_disp','classroom_type','classroom_cap')