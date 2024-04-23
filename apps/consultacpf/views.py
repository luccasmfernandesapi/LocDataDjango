from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, Http404, redirect
from consultacpf.models import PessoaFisica, Email, Naturalidade,  \
    TbEscolaridade, TbCns, TbPis, TbNis, TbCtps, Endereco, EnderecoNovos,  \
    Telefone, TelefoneNovos, EmailNovos, TbEmpregos, VeiculoPessoaFisica
from django.db import connection

# Create your views here.


@login_required
def dadosconsulta(request):
    return render(request, 'consultacpf.html')


@login_required
def listardados(request):
    cpf = request.POST.get("input_name")

    try:
        dados_basicos = PessoaFisica.objects.get(cpf=cpf)
        idade_data = (datetime.now() -
                      dados_basicos.nasc.replace(tzinfo=None))
        idade = int(idade_data.days / 365)

        # Recebe ContatosID
        contatos_id = dados_basicos.contatos_id
        dados_variados = consulta_por_contatosid(contatos_id)
        print(dados_basicos)
        return render(request, 'listardados.html', {'dados_basicos': dados_basicos, 'idade': idade, 'dados': dados_variados})

    except PessoaFisica.DoesNotExist:
        return render(request, 'Erro404CPF.html')


def consulta_por_contatosid(contatos_id):

    dados = {}
    relac_dicts = []
    c = connection.cursor()

    try:
        dados['cns'] = TbCns.objects.get(contatos_id=contatos_id)

    except:
        dados['cns'] = None

    try:
        dados['pis'] = TbPis.objects.get(contatos_id=contatos_id)

    except:
        dados['pis'] = None

    try:
        dados['nis'] = TbNis.objects.get(contatos_id=contatos_id)

    except:
        dados['nis'] = None

    try:
        dados['ctps'] = TbCtps.objects.get(contatos_id=contatos_id)

    except:
        dados['ctps'] = None

    try:
        dados['nat'] = Naturalidade.objects.get(contatos_id=contatos_id)

    except Naturalidade.DoesNotExist:
        dados['nat'] = None

    try:
        dados['esco'] = TbEscolaridade.objects.get(contatos_id=contatos_id)

    except TbEscolaridade.DoesNotExist:
        dados['esco'] = None

    try:
        query = """
                select b.CPF,b.NOME,Convert(varchar(10), b.NASC,103) AS 'DT NASC'
                ,case when b.SEXO = 'F' then 'ESPOSA'
                when b.SEXO = 'M' then 'MARIDO'
                else b.sexo end as 'VINCULO'
                from Produtivo.PESSOA_FISICA as ab
                inner join TopDados.Produtivo.PESSOA_FISICA as b on ab.CONTATOS_ID_CONJUGE = b.CONTATOS_ID
                where (ab.CONTATOS_ID = %s) AND (b.NOME IS NOT NULL)

                UNION

                    select distinct b.CPF_RELACIONAMENTO, b.NOME, Convert(varchar(10), a.NASC, 103) as 'DT NASC', b.VINCULO
                from TopDados.Produtivo.RELACIONAMENTO b
                left join Produtivo.PESSOA_FISICA a on b.CPF_RELACIONAMENTO = a.CPF 
                where(b.CONTATOS_ID = %s) AND(b.NOME IS NOT NULL)

                UNION

                select CPF = '', a.NOME_MAE, 'DT NASC' = '', VINCULO = 'MÃE'
                from Produtivo.PESSOA_FISICA a
                where (a.CONTATOS_ID = %s) and(a.NOME_MAE IS NOT NULL)

                UNION

                select CPF = '', a.NOME_PAI, 'DT NASC' = '', VINCULO = 'PAI'
                from Produtivo.PESSOA_FISICA a
                where (a.CONTATOS_ID = %s) AND(a.NOME_PAI IS NOT NULL)

                UNION

                SELECT b.CPF, b.NOME, Convert(varchar(10), b.NASC, 103) AS 'DT NASC', VINCULO = 'MESMA RESIDENCIA'
                FROM Produtivo.PESSOA_FISICA a
                INNER JOIN Produtivo.PESSOA_FISICA b on b.HOUSEHOLD_ID_2016 = a.HOUSEHOLD_ID_2016
                WHERE(a.CONTATOS_ID = %s) AND(b.CONTATOS_ID <> a.CONTATOS_ID)

                UNION

                SELECT b.CPF, b.NOME, Convert(varchar(10), b.NASC, 103) AS 'DT NASC', VINCULO = 'MESMA RESIDENCIA'
                FROM Produtivo.PESSOA_FISICA a
                INNER JOIN Produtivo.PESSOA_FISICA b on b.HOUSEHOLD_ID = a.HOUSEHOLD_ID
                WHERE(a.CONTATOS_ID = %s) AND(b.CONTATOS_ID <> a.CONTATOS_ID) ORDER BY VINCULO ASC
                """
        c.execute(query, (contatos_id, contatos_id, contatos_id,
                  contatos_id, contatos_id, contatos_id))
        relac = c.fetchall()

        # Convertendo a lista de tuplas em uma lista de dicionários

        relac_dict = [{
            'cpf_relacionamento': item[0],
            'nome': item[1],
            'nasc': item[2],
            'vinculo': item[3]
        }for item in relac]

        unique_relac = {
            item['cpf_relacionamento']: item for item in relac_dict}.values()

        dados['relac'] = list(unique_relac)

    except:
        dados['relac'] = None

    try:
        query2 = """
                SELECT  d.TIPO_LOGRADOURO + ' ' + d.LOGRADOURO + ' ' + d.NUMERO + ' ' + d.COMPLEMENTO AS ENDERECO, d.BAIRRO, e.MUNICIPIO as CIDADE, d.UF, right('00000000' + d.CEP, 8) as CEP 
                FROM[TopDados].[Produtivo].PESSOA_FISICA a
                inner join[TopDados].[Produtivo].[EMPRESAS_SOCIOS] b on a.CONTATOS_ID = b.CONTATOS_ID_SOCIO
                inner join[TopDados].[Produtivo].[EMPRESAS] c on b.EMPRESAS_ID = c.EMPRESAS_ID
                inner join[TopDados].[Produtivo].[EMPRESAS_RECEITA_ESTABELECIMENTO] d on left(right('00000000000000' + c.cnpj, 14), 8) = CNPJ_BASICO and substring(right('00000000000000' + c.CNPJ, 14), 9, 4) = d.CNPJ_ORDEM AND right(c.CNPJ, 2) = d.CNPJ_DV
                Inner join[TopDados].[Produtivo].EMPRESAS_RECEITA_MUNICIPIO e on d.MUNICIPIO = e.CD_MUNICIPIO
                where(a.CONTATOS_ID = %s) AND(d.BAIRRO IS NOT NULL)"""

        # Endereço 1
        end1_data = Endereco.objects.filter(
            contatos_id=contatos_id).values('cep', 'endereco', 'bairro', 'cidade', 'uf').distinct()

        # Endereço 2
        end2_data = EnderecoNovos.objects.filter(
            contatos_id=contatos_id).values('cep', 'endereco', 'bairro', 'cidade', 'uf').distinct()

        # Endereço 3
        c.execute(query2, (contatos_id,))
        endereco = c.fetchall()

        # Convertendo a lista de tuplas em uma lista de dicionários
        endereco_dicts = [{
            'cep': item[4],
            'endereco': item[0],
            'bairro': item[1],
            'cidade': item[2],
            'uf': item[3]
        } for item in endereco]

        # Combinando todos os endereços em uma única lista
        combined_enderecos = list(end1_data) + list(end2_data) + endereco_dicts

        # Removendo duplicatas baseadas no CEP
        unique_enderecos = {
            item['endereco']: item for item in combined_enderecos}.values()

        # Adicionando ao dicionário dados
        dados['end'] = list(unique_enderecos)

    except:
        dados['end'] = None

    try:
        query1 = """
                SELECT c.CNPJ,c.RAZAO_SOCIAL,c.NOME_FANTASIA,
                b.PARTICIPACAO_SOCIO, 
                d.CNAE_DESCRICAO
                FROM [TopDados].[Produtivo].PESSOA_FISICA a 
                inner join [TopDados].[Produtivo].[EMPRESAS_SOCIOS] b on a.CONTATOS_ID = b.CONTATOS_ID_SOCIO
                inner join [TopDados].[Produtivo].[EMPRESAS] c on b.EMPRESAS_ID = c.EMPRESAS_ID
                inner join [TopDados].[Produtivo].[EMPRESAS_CNAE] d on c.CNAE_SG = d.CNAE_SUBCLASSE
                where a.CONTATOS_ID = %s
                union
                SELECT d.CNPJ_BASICO + d.CNPJ_ORDEM + d.CNPJ_DV as CNPJ
                , c.RAZAO_SOCIAL
                , d.NOME_FANTASIA
                , '0.0'
                , e.CNAE_DESCRICAO
                FROM[TopDados].[Produtivo].[EMPRESAS_RECEITA_SOCIOS] a
                inner join Produtivo.PESSOA_FISICA b on a.NOME_SOCIO = b.NOME AND right(left(b.CPF, 9), 6) = right(left(a.[CPF_CNPJ], 9), 6)
                inner join[TopDados].[Produtivo].[EMPRESAS_RECEITA_EMPRESAS] c on a.CNPJ_BASICO = c.CNPJ_BASICO
                inner join[TopDados].[Produtivo].[EMPRESAS_RECEITA_ESTABELECIMENTO] d on a.CNPJ_BASICO = d.CNPJ_BASICO
                inner join[TopDados].[Produtivo].[EMPRESAS_RECEITA_CNAE] e on d.CNAE_PRINCIPAL = e.CNAE
                where b.CONTATOS_ID = %s
                """

        c.execute(query1, (contatos_id, contatos_id))
        empresas = c.fetchall()

        empresas_dict = [{
            'cnpj': item[0],
            'razao': item[1],
            'nome': item[2],
            'participacao': item[3],
            'cnae': item[4]
        } for item in empresas]

        unique_empresa = {
            item['cnpj']: item for item in empresas_dict}.values()

        dados['empresas'] = list(unique_empresa)

    except:
        dados['empresas'] = None

    try:
        # Telefone 1
        tel1 = Telefone.objects.filter(
            contatos_id=contatos_id).values('ddd', 'telefone').distinct()

        # Telefone 2
        tel2 = TelefoneNovos.objects.filter(
            contatos_id=contatos_id).values('ddd', 'telefone').distinct()

        combined_telefones = list(tel1) + list(tel2)

        unique_telefones = {item['telefone']
            : item for item in combined_telefones}.values()

        dados['telefone'] = list(unique_telefones)

    except:
        dados['telefone'] = None

    try:
        email1 = Email.objects.filter(
            contatos_id=contatos_id).values('email').distinct()

        email2 = EmailNovos.objects.filter(
            contatos_id=contatos_id).values('email').distinct()

        combined_emails = list(email1) + list(email2)

        unique_emails = {item['email']: item for item in combined_emails}.values()

        dados['email'] = list(unique_emails)

    except:
        dados['email'] = None

    try:
        empregos = TbEmpregos.objects.filter(
            contatos_id=contatos_id).values('razao_social', 'tipo', 'doc', 'remuneracao', 'cbo').distinct()

        dados['emprego'] = list(empregos)

    except:
        dados['emprego'] = None

    try:
        veiculos = VeiculoPessoaFisica.objects.filter(
            contatos_id=contatos_id)

        dados['veiculos'] = list(veiculos)

    except:
        dados['veiculos'] = None

    return dados
