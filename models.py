from django.db import models

# Create your models here.
class prontuarios(models.Model):
    nome = models.CharField(max_length=50)