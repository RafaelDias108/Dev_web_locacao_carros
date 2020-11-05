from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from conta.models import Conta
from .models import Automovel, Reserva, Locacao

# Register your models here.
class ContaAdmin(UserAdmin):
    list_display = ('email', 'nome', 'endereco', 'telefone')
    list_filter = ('is_admin', 'is_active', 'is_superuser')
    search_fields = ('email', 'nome', 'cpf')
    ordering = ('email','nome')

    filter_horizontal = ()
admin.site.register(Conta, ContaAdmin)

class AutomovelAdmin(admin.ModelAdmin):
    list_display = ('id', 'modelo', 'marca', 'categoria', 'valor_locacao', 'quantidade_estoque')
    list_filter = ('categoria', 'marca')
    search_fields = ('modelo', 'marca', 'categoria')
admin.site.register(Automovel, AutomovelAdmin)

# novos Models
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'veiculo', 'data_locacao', 'valor_previsto')
    list_filter = ('cliente', 'veiculo')
    search_fields = ('cliente', 'veiculo')
admin.site.register(Reserva, ReservaAdmin)

class LocacaoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'veiculo', 'data_locacao', 'valor_final')
    list_filter = ('cliente', 'veiculo')
    search_fields = ('cliente', 'veiculo')
admin.site.register(Locacao, LocacaoAdmin)