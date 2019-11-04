from ..models.Classes import Classes
from rest_framework import serializers
from api.models.Project import Project
from api.models.Group import Group
from api.models.Teacher import Teacher

class ClassesSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:classes-detail")
    project_fk = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    Teacher_fk = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())
    Group_fk = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())
    class Meta:
        model = Classes
        fields = ('id','url','classes_pk','classes_int','project_fk','Teacher_fk','Group_fk')
   
    