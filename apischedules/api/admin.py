from django.contrib import admin
from .models.Project import Project
from .models.Classes import Classes
from .models.Classroom import Classroom
from .models.Group import Group
from .models.Teacher import Teacher
from .models.Asignation import Asignation


admin.site.register(Project)
admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Classes)
admin.site.register(Asignation)
admin.site.register(Classroom)
