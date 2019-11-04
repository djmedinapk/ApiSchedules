from django.db import models

""" 
    Class Teacher 
    Juan David Medina
    Yesid Valencia Gomez
"""
class Teacher(models.Model):

    Teacher_pk = models.IntegerField()                  #primary key del docente
    Teacher_disp = models.TextField(blank=True)         #json-> contiene la disponibilidad del docente

    def __str__(self):
        return str(self.Teacher_pk)