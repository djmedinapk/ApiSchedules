from django.db import models

""" 
    Class Project 
    Juan David Medina
    Yesid Valencia Gomez
"""
class Project(models.Model):

    project_pk = models.IntegerField()                      #primary key del proyecto
    project_state = models.CharField(max_length = 255)      #estado del proyecto

    def __str__(self):
        return str(self.id)
    
    # @property
    # def asignations(self):
    #     return self.asignation_set.all()

