from ..models.Teacher import Teacher
from rest_framework import serializers

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:teacher-detail")
    class Meta:
        model = Teacher
        fields = ('id','url','Teacher_pk','Teacher_disp')