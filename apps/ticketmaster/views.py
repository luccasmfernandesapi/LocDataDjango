
from django.shortcuts import render
from ticketmaster.models import TmAereoStatus, TmAereoTrx
from django.core.paginator import Paginator
from django.db.models import Prefetch
from consultacpf.models import Endereco, EmailNovos, Telefone

# Create your views here.


def home(request):

    cpf = request.GET.get('cpf', '')
    status = request.GET.get('status', '')

    transacoes = TmAereoTrx.objects.select_related('status_transacao', 'frequent_flyer_number').prefetch_related(
        Prefetch('frequent_flyer_number__enderecos',
                 queryset=Endereco.objects.distinct()),
        Prefetch('frequent_flyer_number__emails',
                 queryset=EmailNovos.objects.distinct()),
        Prefetch('frequent_flyer_number__telefones',
                 queryset=Telefone.objects.distinct())
    ).order_by('transactiondate')

    if cpf:
        transacoes = transacoes.filter(
            status_transacao__frequent_flyer_number__icontains=cpf)

    if status:
        transacoes = transacoes.filter(status_transacao__status=status)

    print(cpf)
    current_page = request.GET.get('page', 1)
    paginator = Paginator(transacoes, 20)
    page_obj = paginator.get_page(current_page)

    return render(request, "home.html", {'transacoes': page_obj, 'cpf': cpf, 'status': status, 'user': request.user})


def get_transacoes_anteriores(frequent_flyer_number, trx_id):
    return TmAereoTrx.objects.filter(
        status_transacao__frequent_flyer_number=frequent_flyer_number
    ).exclude(id=trx_id).order_by('-transactiondate')
