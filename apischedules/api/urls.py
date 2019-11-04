from django.urls import path, include
from api.views.ProjectView import *
from api.views.TeacherView import *
from api.views.GroupView import *
from api.views.ClassesView import *
from api.views.ClassroomView import *
from api.views.AsignationView import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('project',ProjectView)
router.register('teacher',TeacherView)
router.register('group',Groupview)
router.register('classes',ClassesView)
router.register('classroom',ClassroomView)
router.register('asignation',AsignationView)


urlpatterns = [
    path('',include(router.urls))
    # path('project/', ProjectList.as_view(), name='projects'),
    # path('project/<int:pk>/', ProjectDetail.as_view()),
    # path('teacher/', TeacherList.as_view(), name='teachers'),
    # path('teacher/<int:pk>/', TeacherDetail.as_view()),
    # path('group/', GroupList.as_view(), name='groups'),
    # path('group/<int:pk>/', GroupDetail.as_view()),
    # path('classes/', ClassesList.as_view(), name='classes'),
    # path('classes/<int:pk>/', ClassesDetail.as_view()),
]