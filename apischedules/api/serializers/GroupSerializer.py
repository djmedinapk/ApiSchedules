from ..models.Group import Group
from rest_framework import serializers

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:group-detail")
    class Meta:
        model = Group
        fields = ('id','url','Group_pk','Group_size')