from django.db import models

# Create your models here.
class prontuarios(models.Model):
    nome = models.CharField(max_length=50)
   

# Create your models here.
class matricula(models.Model):
    nome = models.CharField(max_length=50)
    data = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    nis = models.CharField(max_length=50)
    busca_esportiva = models.CharField(max_length=50)
    ndemanda_espontanea = models.CharField(max_length=50)
    encaminhamento = models.CharField(max_length=50)
    busca_ativa = models.BooleanField(default=True)
    encaminhamento_politicas = models.CharField(max_length=50)
    perfil_etario_0_6 = models.CharField(max_length=50)
    perfil_etario_7_14 = models.CharField(max_length=50)
    perfil_etario_15_17 = models.CharField(max_length=50)
    perfil_etario_18_29 = models.CharField(max_length=50)
    perfil_etario_30_59 = models.CharField(max_length=50)
    perfil_etario_60 = models.CharField(max_length=50)







    
    
    


