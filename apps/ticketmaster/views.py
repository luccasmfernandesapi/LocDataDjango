
from django.shortcuts import render
from ticketmaster.models import TmAereoStatus, TmAereoTrx
from django.core.paginator import Paginator

# Create your views here.


def home(request):

    cpf = request.GET.get('cpf', '')
    status = request.GET.get('status', '')

    transacoes = TmAereoTrx.objects.prefetch_related(
        "status_transacao", "frequent_flyer_number__enderecos").order_by('transactiondate')

    if cpf:
        transacoes = transacoes.filter(
            status_transacao__frequent_flyer_number__icontains=cpf)

    if status:
        transacoes = transacoes.filter(status_transacao__status=status)

    current_page = request.GET.get('page', 1)
    paginator = Paginator(transacoes, 10)
    page_obj = paginator.get_page(current_page)

    return render(request, "home.html", {'transacoes': page_obj, 'cpf': cpf, 'status': status, 'user': request.user})


def PegarEndereco():
    ...
