from django.db import models

""" 
    Class Group 
    Juan David Medina
    Yesid Valencia Gomez
"""
class Group(models.Model):

    Group_pk = models.IntegerField()                    #primary key del grupo
    Group_size = models.IntegerField(blank=True)        #tamaño del grupo ( Cantidad de estudiante)

    def __str__(self):
        return str(self.Group_pk)