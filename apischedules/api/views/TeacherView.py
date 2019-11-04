from rest_framework import generics, viewsets
from..models.Teacher import Teacher
from api.serializers.TeacherSerializer import TeacherSerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt



class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

# class TeacherList(generics.ListCreateAPIView):

#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer

#     def get_object(self):
#         queryset = self.get_queryset()
#         obj = get_object_or_404(
#             queryset,
#             pk= self.kwargs['pk'],
#         )
#         return obj

# class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer

#     @csrf_exempt 
#     def teacher_detail(request, pk):
#         try:
#             teacher = Teacher.objects.get(pk=pk)
#         except Teacher.DoesNotExist:
#             return HttpResponse(status=404)

#         if request.method == 'GET':
#             serializer = TeacherSerializer(teacher)
#             return JsonResponse(serializer.data)

#         elif request.method == 'PUT':
#             data = JSONParser().parse(request)
#             serializer = TeacherSerializer(teacher, data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse(serializer.data)
#             return JsonResponse(serializer.errors, status=400)

#         elif request.method == 'DELETE':
#             teacher.delete()
#             return HttpResponse(status=204)