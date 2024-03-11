from django.db import models
class Comentario (models.model):

    id = models.AutoField(primary_key=True)

    titulo= models.CharField(max_length-100)

    texto= models.textField()

    data= models.DateTimeField(auto_now_add=True)

    hora= TimeField(auto_now_add=True)

    