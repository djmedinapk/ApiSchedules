from rest_framework import generics, viewsets
from ..models.Project import Project
from ..serializers.ProjectSerializer import ProjectSerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# class ProjectList(generics.ListCreateAPIView):

#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

#     def get_object(self):
#         queryset = self.get_queryset()
#         obj = get_object_or_404(
#             queryset,
#             pk= self.kwargs['pk'],
#         )
#         return obj


# class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

#     @csrf_exempt 
#     def project_detail(request, pk):
#         try:
#             project = Project.objects.get(pk=pk)
#         except Project.DoesNotExist:
#             return HttpResponse(status=404)
    
#         if request.method == 'GET':
#             serializer = ProjectSerializer(project)
#             return JsonResponse(serializer.data)
    
#         elif request.method == 'PUT':
#             data = JSONParser().parse(request)
#             serializer = ProjectSerializer(project, data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse(serializer.data)
#             return JsonResponse(serializer.errors, status=400)
    
#         elif request.method == 'DELETE':
#             project.delete()
#             return HttpResponse(status=204)