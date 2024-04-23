from django.contrib import admin
from consultacpf.models import PessoaFisica, Ocupacao


class PessoaFisicaAdmin(admin.ModelAdmin):
    search_fields = ['cpf__exact']


# Register your models here.
admin.site.register(PessoaFisica, PessoaFisicaAdmin)
admin.site.register(Ocupacao)
