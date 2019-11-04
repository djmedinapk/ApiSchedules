from django.db import models
from .Classroom import Classroom
from .Classes import Classes
from .Project import Project

""" 
    Class Classes 
    Juan David Medina
    Yesid Valencia Gomez
"""
class Asignation(models.Model):

    asignation_pk = models.IntegerField()                                   #primary key de la asigancion
    asignation_start = models.CharField(max_length = 255)                                   #inicio de la asignacion hora
    asignation_end = models.CharField(max_length = 255)                                     #fin de la asignacion hora
    asignation_day = models.CharField(max_length = 255)                                     #dia de la asignacion
    classroom_fk = models.ForeignKey(Classroom, on_delete=models.CASCADE)   #salon que se asigno
    classes_fk = models.ForeignKey(Classes, on_delete=models.CASCADE)       #clase que se asigno
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='asignations')       #projecto que se asigno


    def __str__(self):
        return str(self.asignation_pk)