from ..models.Project import Project
from rest_framework import serializers
from api.serializers.AsignationSerializer import AsignationSerializer

class ProjectSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:project-detail")
    #asignations = AsignationSerializer(many=True)
    class Meta:
        model = Project
        fields = ('id','url','project_pk','project_state')
