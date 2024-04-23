from datetime import datetime
import pytz
from django.shortcuts import render
from ticketmaster.models import TmAereoStatus, TmAereoTrx
from django.core.paginator import Paginator

# Create your views here.

# Definindo o fuso horário para 'America/Sao_Paulo'
tz = pytz.timezone('America/Sao_Paulo')


def home(request):
    data_inicio = tz.localize(datetime(2024, 4, 1))

    transacoes = TmAereoTrx.objects.filter(transactiondate__gt=data_inicio).select_related(
        "frequent_flyer_number", "status_transacao").order_by('transactiondate')

    current_page = request.GET.get('page', 1)
    paginator = Paginator(transacoes, 10)
    page_obj = paginator.get_page(current_page)

    return render(request, "home.html", {'transacoes': page_obj})
