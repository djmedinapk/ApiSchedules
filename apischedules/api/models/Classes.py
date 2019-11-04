from django.db import models
from .Project import Project
from .Teacher import Teacher
from .Group import Group

""" 
    Class Classes 
    Juan David Medina
    Yesid Valencia Gomez
"""
class Classes(models.Model):
    
    project_fk = models.ForeignKey(Project, on_delete=models.CASCADE)   #Projecto al que pertenece la clase
    Teacher_fk = models.ForeignKey(Teacher, on_delete=models.CASCADE)   #Teacher asignadoa  la clase
    Group_fk = models.ForeignKey(Group, on_delete=models.CASCADE)       #Grupo asignado a la clase
    classes_pk = models.IntegerField()                                  #primary key de la clase
    classes_int = models.IntegerField()                                 #cantidad de horas en total que se dicataran en al clase


    def __str__(self):
        return str(self.classes_pk)


    