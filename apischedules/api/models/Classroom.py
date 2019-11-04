from django.db import models

""" 
    Class Classroom 
    Juan David Medina
    Yesid Valencia Gomez
"""
class Classroom(models.Model):

    classroom_pk = models.IntegerField()                    #priamry key del salon
    classroom_disp = models.TextField(blank=True)           #json-> disponibilidad del salon
    classroom_type = models.CharField(max_length = 255)     #tipo de salon
    classroom_cap = models.IntegerField()                   #capacidad


    def __str__(self):
        return str(self.classroom_pk)