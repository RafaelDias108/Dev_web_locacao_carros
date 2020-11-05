from django.db import models
from conta.models import Conta

# Create your models here.
class Automovel(models.Model):
    CATEGORIA_VEICULOS = [
        ('SUV', 'SUV'),
        ('Passeio', 'Passeio'),
        ('Caminhonete', 'Caminhonete'),
        ('Carga', 'Carga')
    ]

    TIPO_COMBUST = [
        ('Gasolina', 'Gasolina'),
        ('Alcool', 'Alcool'),
        ('Diesel', 'Diesel')
    ]

    modelo = models.CharField(max_length=100, blank=False, null=False)
    marca = models.CharField(max_length=100, blank=False, null=False)
    descricao = models.CharField(max_length=300, blank=False, null=False)
    categoria = models.CharField(max_length=20, blank=False, null=False, choices=CATEGORIA_VEICULOS)
    cor = models.CharField(max_length=50, blank=False, null=False)
    numero_portas = models.PositiveIntegerField(blank=False, null=False)
    tipo_combustivel = models.CharField(max_length=20, blank=False, null=False, choices=TIPO_COMBUST)
    quilometragem = models.PositiveIntegerField(blank=False, null=False)
    renavam = models.CharField(max_length=50, blank=False, null=False)
    chassi = models.CharField(max_length=50, blank=False, null=False)
    valor_locacao = models.DecimalField(max_digits = 5, decimal_places = 2)
    quantidade_estoque = models.PositiveIntegerField(blank=False, null=False)
    

    def __str__(self):
        return self.modelo

class Reserva(models.Model):
    data_locacao = models.DateField(verbose_name = 'Data de início da locação', blank=False, null=False)
    hora_locacao = models.TimeField(verbose_name = 'Hora de início da locação', blank=False, null=False)
    data_devolucao = models.DateField(verbose_name = 'Data de término da locação', blank=False, null=False)
    hora_devolucao = models.TimeField(verbose_name = 'Hora de término da locação', blank=False, null=False)
    valor_previsto = models.DecimalField(verbose_name = 'Valor Previsto', max_digits = 5, decimal_places = 2, blank=False, null=False)
    veiculo = models.ForeignKey('Automovel', blank=False, null=False, on_delete=models.CASCADE)
    cliente = models.ForeignKey('conta.Conta', blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.veiculo.modelo + " - " + self.cliente.nome


class Locacao(models.Model):
    data_locacao = models.DateField(blank=False, null=False)
    hora_locacao = models.TimeField(blank=False, null=False)
    data_devolucao = models.DateField(blank=False, null=False)
    hora_devolucao = models.TimeField(blank=False, null=False)
    valor_final = models.DecimalField(max_digits = 5, decimal_places = 2, blank=False, null=False)
    veiculo = models.ForeignKey('Automovel', blank=False, null=False, on_delete=models.CASCADE)
    cliente = models.ForeignKey('conta.Conta', blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.veiculo.modelo + " - " + self.cliente.nome