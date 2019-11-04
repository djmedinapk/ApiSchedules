from rest_framework import generics,viewsets
from ..models.Classes import Classes
from ..serializers.ClassesSerializer import ClassesSerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

class ClassesView(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer

# class ClassesList(generics.ListCreateAPIView):

#     @csrf_exempt 
#     def get(self, request, format=None):
#         clasees = Classes.objects.all()
#         serializer = ClassesSerializer(clasees, many=True)
#         return JsonResponse(serializer.data,safe=False)

#     @csrf_exempt 
#     def post(self, request, format=None):
#         serializer = ClassesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# class ClassesDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Classes.objects.all()
#     serializer_class = ClassesSerializer

#     @csrf_exempt 
#     def clasees_detail(request, pk):
#         try:
#             clasees = Classes.objects.get(pk=pk)
#         except Classes.DoesNotExist:
#             return HttpResponse(status=404)
    
#         if request.method == 'GET':
#             serializer = ClassesSerializer(clasees)
#             return JsonResponse(serializer.data)
    
#         elif request.method == 'PUT':
#             data = JSONParser().parse(request)
#             serializer = ClassesSerializer(clasees, data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse(serializer.data)
#             return JsonResponse(serializer.errors, status=400)
    
#         elif request.method == 'DELETE':
#             clasees.delete()
#             return HttpResponse(status=204)