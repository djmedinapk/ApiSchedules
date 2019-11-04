from rest_framework import generics, viewsets
from ..models.Group import Group
from ..serializers.GroupSerializer import GroupSerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


class Groupview(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# class GroupList(generics.ListCreateAPIView):

#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

#     def get_object(self):
#         queryset = self.get_queryset()
#         obj = get_object_or_404(
#             queryset,
#             pk= self.kwargs['pk'],
#         )
#         return obj


# class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

#     @csrf_exempt 
#     def group_detail(request, pk):
#         try:
#             group = Group.objects.get(pk=pk)
#         except Group.DoesNotExist:
#             return HttpResponse(status=404)
    
#         if request.method == 'GET':
#             serializer = GroupSerializer(group)
#             return JsonResponse(serializer.data)
    
#         elif request.method == 'PUT':
#             data = JSONParser().parse(request)
#             serializer = GroupSerializer(group, data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse(serializer.data)
#             return JsonResponse(serializer.errors, status=400)
    
#         elif request.method == 'DELETE':
#             group.delete()
#             return HttpResponse(status=204)