from django.db import models
from django.contrib.auth import get_user_model


class Chassi(models.Model):
    numero = models.CharField('Chassi', max_length=16, help_text='Máximo:16 caracteres')

    class Meta:
        verbose_name = "Chassi"
        verbose_name_plural = 'Chassis'

    def __str__(self):
        return self.numero


class Montadora(models.Model):
    nome = models.CharField('Nome', max_length=50)

    class Meta:
        verbose_name = "Montadora"
        verbose_name_plural = 'Montadoras'

    def __str__(self):
        return self.nome


class Carro(models.Model):
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
    modelo = models.CharField('Modelo', max_length=30, help_text='Máximo:30 caracteres')
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    descricao = models.TextField('Descrição', max_length=500, help_text='Máximo:500 caracteres')
    montadora = models.ForeignKey(Montadora, on_delete=models.CASCADE)
    motoristas = models.ManyToManyField(get_user_model())

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'{self.montadora} {self.modelo}'
