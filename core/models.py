from django.db import models
from stdimage.models import StdImageField


class Base(models.Model):
    criados = models.DateField("Criação", auto_now_add=True)
    modificado = models.DateField("Atualização", auto_now=True)
    ativo = models.BooleanField("Atuvi", default=True)
    
    class Meta:
        abstract = True
        
class Servico(Base):
    ICONE_CHOISES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Grafico'),
        ('lni-users', 'Usuarios'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField('Servico', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOISES)
    
    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"
        
    def __str__(self):
        return self.servico