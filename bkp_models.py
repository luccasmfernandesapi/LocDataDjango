# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApiTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(max_length=500)
    expires_at = models.DateTimeField()
    user = models.ForeignKey('ApiUsuarios', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Api_TOKENS'


class ApiUsuarios(models.Model):
    # Field name made lowercase.
    user_id = models.BigAutoField(db_column='User_id', primary_key=True)
    # Field name made lowercase.
    usuario = models.CharField(
        db_column='Usuario', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    nome_empresa = models.CharField(
        db_column='Nome_empresa', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    cod_funcao = models.IntegerField(
        db_column='Cod_funcao', blank=True, null=True)
    # Field name made lowercase.
    senha = models.CharField(
        db_column='Senha', max_length=1000, blank=True, null=True)
    salt = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Api_Usuarios'


class ApiLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(ApiUsuarios, models.DO_NOTHING)
    location = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    nome_empresa = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Api_log'


class BasePat(models.Model):
    cnpj = models.CharField(max_length=550, blank=True, null=True)
    tipo_estab = models.CharField(max_length=550, blank=True, null=True)
    uf = models.CharField(max_length=550, blank=True, null=True)
    func_por_uf = models.CharField(max_length=550, blank=True, null=True)
    qtd_servico_proprio = models.CharField(
        max_length=550, blank=True, null=True)
    qtd_cesta_alimentos = models.CharField(
        max_length=550, blank=True, null=True)
    qtd_refeicao_transportada = models.CharField(
        max_length=550, blank=True, null=True)
    qtd_refeicao_convenio = models.CharField(
        max_length=550, blank=True, null=True)
    qtd_adm_cozinha = models.CharField(max_length=550, blank=True, null=True)
    qtd_alimentacao_convenio = models.CharField(
        max_length=550, blank=True, null=True)
    qtd_diaria_almoco = models.CharField(max_length=550, blank=True, null=True)
    qtd_diaria_jantar = models.CharField(max_length=550, blank=True, null=True)
    qtd_diaria_refeicao_noturna = models.CharField(
        max_length=550, blank=True, null=True)
    qtd_diaria_desjejum = models.CharField(
        max_length=550, blank=True, null=True)
    qtd_diaria_merenda = models.CharField(
        max_length=550, blank=True, null=True)
    qtd_func_ate_5sm = models.CharField(max_length=550, blank=True, null=True)
    qtd_func_acima_5sm = models.CharField(
        max_length=550, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BASE_PAT'


class BigdataConsulta(models.Model):
    # Field name made lowercase.
    id_consulta = models.BigIntegerField(db_column='ID_CONSULTA')
    # Field name made lowercase.
    dt_consulta = models.DateTimeField(
        db_column='DT_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    ds_token = models.CharField(
        db_column='DS_TOKEN', max_length=1000, blank=True, null=True)
    # Field name made lowercase.
    nu_documento = models.CharField(db_column='NU_DOCUMENTO', max_length=14)
    # Field name made lowercase.
    ds_json_resultado = models.TextField(
        db_column='DS_JSON_RESULTADO', blank=True, null=True)
    # Field name made lowercase.
    ic_cadastral = models.CharField(db_column='IC_CADASTRAL', max_length=1)
    # Field name made lowercase.
    ic_obito = models.CharField(db_column='IC_OBITO', max_length=1)
    # Field name made lowercase.
    ic_erro = models.CharField(db_column='IC_ERRO', max_length=1)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(db_column='DT_INCLUSAO')
    # Field name made lowercase.
    ic_retorno_tratado = models.CharField(
        db_column='IC_RETORNO_TRATADO', max_length=1)
    # Field name made lowercase.
    id_usuario_consultou = models.IntegerField(
        db_column='ID_USUARIO_CONSULTOU', blank=True, null=True)
    # Field name made lowercase.
    ds_token_id = models.CharField(
        db_column='DS_TOKEN_ID', max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BIGDATA_CONSULTA'


class BigdataConsultasDeParaItensOrdem(models.Model):
    # Field name made lowercase.
    ds_item = models.CharField(db_column='DS_ITEM', max_length=718)
    # Field name made lowercase.
    ordem = models.IntegerField(db_column='ORDEM', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BIGDATA_CONSULTAS_DE_PARA_ITENS_ORDEM'


class BigdataConsultasEmpregos(models.Model):
    # Field name made lowercase.
    id_consulta_fk = models.BigIntegerField(db_column='ID_CONSULTA_FK')
    # Field name made lowercase.
    nu_documento = models.CharField(db_column='NU_DOCUMENTO', max_length=14)
    # Field name made lowercase.
    dt_consulta = models.DateTimeField(
        db_column='DT_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    doc = models.TextField(db_column='DOC', blank=True, null=True)
    # Field name made lowercase.
    nome_pessoa = models.TextField(
        db_column='NOME_PESSOA', blank=True, null=True)
    # Field name made lowercase.
    nome = models.TextField(db_column='NOME', blank=True, null=True)
    # Field name made lowercase.
    renda = models.TextField(db_column='RENDA', blank=True, null=True)
    # Field name made lowercase.
    cbo = models.TextField(db_column='CBO', blank=True, null=True)
    # Field name made lowercase.
    data_inicio = models.TextField(
        db_column='DATA_INICIO', blank=True, null=True)
    # Field name made lowercase.
    data_termino = models.TextField(
        db_column='DATA_TERMINO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BIGDATA_CONSULTAS_EMPREGOS'


class BigdataConsultasRelacionamentosEmpresa(models.Model):
    # Field name made lowercase.
    id_consulta_fk = models.BigIntegerField(db_column='ID_CONSULTA_FK')
    # Field name made lowercase.
    nu_documento = models.CharField(db_column='NU_DOCUMENTO', max_length=14)
    # Field name made lowercase.
    dt_consulta = models.DateTimeField(
        db_column='DT_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    cnpj = models.TextField(db_column='CNPJ', blank=True, null=True)
    # Field name made lowercase.
    nome = models.TextField(db_column='NOME', blank=True, null=True)
    # Field name made lowercase.
    vinculo = models.TextField(db_column='VINCULO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BIGDATA_CONSULTAS_RELACIONAMENTOS_EMPRESA'


class BigdataConsultasRetornoCadastral(models.Model):
    # Field name made lowercase.
    id_consulta_fk = models.BigIntegerField(db_column='ID_CONSULTA_FK')
    # Field name made lowercase.
    nu_documento = models.CharField(db_column='NU_DOCUMENTO', max_length=14)
    # Field name made lowercase.
    dt_consulta = models.DateTimeField(
        db_column='DT_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    tipo_retorno = models.TextField(
        db_column='TIPO_RETORNO', blank=True, null=True)
    # Field name made lowercase.
    id_consulta = models.TextField(
        db_column='ID_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    cpf = models.TextField(db_column='CPF', blank=True, null=True)
    # Field name made lowercase.
    nome = models.TextField(db_column='NOME', blank=True, null=True)
    # Field name made lowercase.
    dt_nascimento = models.TextField(
        db_column='DT_NASCIMENTO', blank=True, null=True)
    # Field name made lowercase.
    idade = models.TextField(db_column='IDADE', blank=True, null=True)
    # Field name made lowercase.
    signo = models.TextField(db_column='SIGNO', blank=True, null=True)
    # Field name made lowercase.
    sexo = models.TextField(db_column='SEXO', blank=True, null=True)
    # Field name made lowercase.
    mae = models.TextField(db_column='MAE', blank=True, null=True)
    # Field name made lowercase.
    pai = models.TextField(db_column='PAI', blank=True, null=True)
    # Field name made lowercase.
    situacao_cadastral = models.TextField(
        db_column='SITUACAO_CADASTRAL', blank=True, null=True)
    # Field name made lowercase.
    dt_situacao_cadastral = models.TextField(
        db_column='DT_SITUACAO_CADASTRAL', blank=True, null=True)
    # Field name made lowercase.
    pis = models.TextField(db_column='PIS', blank=True, null=True)
    # Field name made lowercase.
    estado_civil = models.TextField(
        db_column='ESTADO_CIVIL', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BIGDATA_CONSULTAS_RETORNO_CADASTRAL'


class BigdataConsultasRetornoEmail(models.Model):
    # Field name made lowercase.
    id_consulta_fk = models.BigIntegerField(db_column='ID_CONSULTA_FK')
    # Field name made lowercase.
    nu_documento = models.CharField(db_column='NU_DOCUMENTO', max_length=14)
    # Field name made lowercase.
    dt_consulta = models.DateTimeField(
        db_column='DT_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    email = models.TextField(db_column='EMAIL', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BIGDATA_CONSULTAS_RETORNO_EMAIL'


class BigdataConsultasRetornoEndereco(models.Model):
    # Field name made lowercase.
    id_consulta_fk = models.BigIntegerField(db_column='ID_CONSULTA_FK')
    # Field name made lowercase.
    nu_documento = models.CharField(db_column='NU_DOCUMENTO', max_length=14)
    # Field name made lowercase.
    dt_consulta = models.DateTimeField(
        db_column='DT_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    tipo_logradouro = models.TextField(
        db_column='TIPO_LOGRADOURO', blank=True, null=True)
    # Field name made lowercase.
    logradouro = models.TextField(
        db_column='LOGRADOURO', blank=True, null=True)
    # Field name made lowercase.
    numero = models.TextField(db_column='NUMERO', blank=True, null=True)
    # Field name made lowercase.
    complemento = models.TextField(
        db_column='COMPLEMENTO', blank=True, null=True)
    # Field name made lowercase.
    bairro = models.TextField(db_column='BAIRRO', blank=True, null=True)
    # Field name made lowercase.
    cidade = models.TextField(db_column='CIDADE', blank=True, null=True)
    # Field name made lowercase.
    uf = models.TextField(db_column='UF', blank=True, null=True)
    # Field name made lowercase.
    cep = models.TextField(db_column='CEP', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BIGDATA_CONSULTAS_RETORNO_ENDERECO'


class BigdataConsultasRetornoRelacionamento(models.Model):
    # Field name made lowercase.
    id_consulta_fk = models.BigIntegerField(db_column='ID_CONSULTA_FK')
    # Field name made lowercase.
    nu_documento = models.CharField(db_column='NU_DOCUMENTO', max_length=14)
    # Field name made lowercase.
    dt_consulta = models.DateTimeField(
        db_column='DT_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    cpf = models.TextField(db_column='CPF', blank=True, null=True)
    # Field name made lowercase.
    nome = models.TextField(db_column='NOME', blank=True, null=True)
    # Field name made lowercase.
    vinculo = models.TextField(db_column='VINCULO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BIGDATA_CONSULTAS_RETORNO_RELACIONAMENTO'


class BigdataConsultasRetornoTelefone(models.Model):
    # Field name made lowercase.
    id_consulta_fk = models.BigIntegerField(db_column='ID_CONSULTA_FK')
    # Field name made lowercase.
    nu_documento = models.CharField(db_column='NU_DOCUMENTO', max_length=14)
    # Field name made lowercase.
    dt_consulta = models.DateTimeField(
        db_column='DT_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    ddd = models.TextField(db_column='DDD', blank=True, null=True)
    # Field name made lowercase.
    telefone = models.TextField(db_column='TELEFONE', blank=True, null=True)
    # Field name made lowercase.
    tipo = models.TextField(db_column='TIPO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BIGDATA_CONSULTAS_RETORNO_TELEFONE'


class BigdataConsultasTratadas(models.Model):
    id = models.BigIntegerField(db_column='ID')  # Field name made lowercase.
    # Field name made lowercase.
    id_pai_fk = models.BigIntegerField(
        db_column='ID_PAI_FK', blank=True, null=True)
    # Field name made lowercase.
    id_consulta_fk = models.IntegerField(db_column='ID_CONSULTA_FK')
    # Field name made lowercase.
    ds_key = models.CharField(db_column='DS_KEY', max_length=100)
    # Field name made lowercase.
    ds_value = models.TextField(db_column='DS_VALUE', blank=True, null=True)
    # Field name made lowercase.
    ds_type = models.CharField(db_column='DS_TYPE', max_length=10)
    # Field name made lowercase.
    ic_tratado = models.CharField(db_column='IC_TRATADO', max_length=1)

    class Meta:
        managed = False
        db_table = 'BIGDATA_CONSULTAS_TRATADAS'


class BigdataToken(models.Model):
    # Field name made lowercase.
    id_token = models.IntegerField(db_column='ID_TOKEN')
    # Field name made lowercase.
    dt_data_token = models.DateTimeField(db_column='DT_DATA_TOKEN')
    # Field name made lowercase.
    ds_token = models.CharField(db_column='DS_TOKEN', max_length=1000)
    # Field name made lowercase.
    ds_token_id = models.CharField(db_column='DS_TOKEN_ID', max_length=100)

    class Meta:
        managed = False
        db_table = 'BIGDATA_TOKEN'


class CadastrosOrigem(models.Model):
    # Field name made lowercase.
    cadastro_id = models.SmallIntegerField(
        db_column='CADASTRO_ID', primary_key=True)
    # Field name made lowercase.
    descricao = models.CharField(
        db_column='DESCRICAO', unique=True, max_length=100)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(db_column='DT_INCLUSAO')
    # Field name made lowercase.
    rank = models.IntegerField(db_column='RANK', blank=True, null=True)
    # Field name made lowercase.
    id_peso = models.SmallIntegerField(
        db_column='ID_PESO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CADASTROS_ORIGEM'


class CadastroOrigemSerasa(models.Model):
    # Field name made lowercase.
    cadastro_id_srs = models.AutoField(
        db_column='CADASTRO_ID_SRS', primary_key=True, db_comment='- C¾digo do cadastro ID do ser')
    # Field name made lowercase.
    cadastro_sigla = models.CharField(
        db_column='CADASTRO_SIGLA', max_length=5, blank=True, null=True, db_comment='- Sigla do Cadastro')
    # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=80,
                                 blank=True, null=True, db_comment='- DescriþÒo da Origem')

    class Meta:
        managed = False
        db_table = 'CADASTRO_ORIGEM_SERASA'


class CatOutubro2021Mg1(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    cpf = models.CharField(
        db_column='CPF', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    razao_social = models.CharField(
        db_column='RAZAO_SOCIAL', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    tipo = models.CharField(
        db_column='TIPO', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    doc = models.CharField(
        db_column='DOC', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    nome = models.CharField(
        db_column='NOME', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    remuneracao = models.IntegerField(db_column='REMUNERACAO')
    # Field name made lowercase.
    cbo = models.CharField(
        db_column='CBO', max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CAT - OUTUBRO 2021 - MG (1)'


class Cbo2002Rev2009(models.Model):
    # Field name made lowercase.
    cd_cbo = models.CharField(
        db_column='CD_CBO', max_length=6, blank=True, null=True)
    # Field name made lowercase.
    descricao = models.CharField(
        db_column='DESCRICAO', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    tipo = models.CharField(
        db_column='TIPO', max_length=8, blank=True, null=True)
    # Field name made lowercase.
    cbo_novo = models.CharField(
        db_column='CBO_NOVO', max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CBO_2002_REV_2009'


class ClasseSocial(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', blank=True, null=True)
    # Field name made lowercase.
    classe_social = models.CharField(
        db_column='CLASSE_SOCIAL', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    sub_classe_social = models.CharField(
        db_column='SUB_CLASSE_SOCIAL', max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CLASSE_SOCIAL'


class CnaeSec(models.Model):
    # Field name made lowercase.
    empresas_id = models.IntegerField(
        db_column='EMPRESAS_ID', blank=True, null=True)
    # Field name made lowercase.
    cnae = models.CharField(
        db_column='CNAE', max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CNAE_SEC'


class CodAeroporto(models.Model):
    # Field name made lowercase.
    iata = models.CharField(
        db_column='IATA', max_length=3, blank=True, null=True)
    # Field name made lowercase.
    icao = models.CharField(
        db_column='ICAO', max_length=4, blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    nome_do_aeroporto = models.CharField(
        db_column='NOME DO AEROPORTO', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    cidade = models.CharField(
        db_column='CIDADE', max_length=19, blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'COD_AEROPORTO'


class ContatosMaiorCemAnos(models.Model):
    # Field name made lowercase.
    cpf = models.CharField(
        db_column='CPF', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CONTATOS_MAIOR_CEM_ANOS'


class ContatosMenorIdade(models.Model):
    # Field name made lowercase.
    cpf = models.CharField(
        db_column='CPF', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CONTATOS_MENOR_IDADE'


class ContatosNascPresumido(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    nasc = models.DateTimeField(db_column='Nasc', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Contatos_Nasc_Presumido'


class DescricaoEndscore(models.Model):
    # Field name made lowercase.
    classificacao = models.CharField(
        db_column='CLASSIFICACAO', max_length=5, blank=True, null=True)
    # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=50)

    class Meta:
        managed = False
        db_table = 'DESCRICAO_ENDSCORE'


class DescricaoFonescore(models.Model):
    # Field name made lowercase.
    classificacao = models.CharField(
        db_column='CLASSIFICACAO', max_length=5, blank=True, null=True)
    # Field name made lowercase.
    descricao = models.CharField(
        db_column='DESCRICAO', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    prioridade = models.CharField(
        db_column='PRIORIDADE', max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DESCRICAO_FONESCORE'


class DeParaServidores(models.Model):
    # Field name made lowercase.
    descricao = models.CharField(
        db_column='DESCRICAO', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    cod_serv = models.CharField(
        db_column='COD_SERV', max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DE_PARA_SERVIDORES'


class Email(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', blank=True, null=True)
    # Field name made lowercase.
    email = models.CharField(
        db_column='EMAIL', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    prioridade = models.BigIntegerField(
        db_column='PRIORIDADE', blank=True, null=True)
    # Field name made lowercase.
    email_score = models.CharField(
        db_column='EMAIL_SCORE', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    email_pessoal = models.CharField(
        db_column='EMAIL_PESSOAL', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    email_duplicado = models.CharField(
        db_column='EMAIL_DUPLICADO', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    blacklist = models.CharField(
        db_column='BLACKLIST', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    estrutura = models.CharField(
        db_column='ESTRUTURA', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    status_vt = models.CharField(
        db_column='STATUS_VT', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    dominio = models.CharField(
        db_column='DOMINIO', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    mapas = models.IntegerField(db_column='MAPAS', blank=True, null=True)
    # Field name made lowercase.
    peso = models.IntegerField(db_column='PESO', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id = models.CharField(
        db_column='CADASTRO_ID', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMAIL'


class EmailsBloqueadosProcon(models.Model):
    # Field name made lowercase.
    emails_bloqueados_id = models.AutoField(
        db_column='EMAILS_BLOQUEADOS_ID', primary_key=True)
    # Field name made lowercase.
    email = models.CharField(
        db_column='EMAIL', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    dt_cadastro = models.DateTimeField(
        db_column='DT_CADASTRO', blank=True, null=True)
    # Field name made lowercase.
    dt_limite = models.DateTimeField(
        db_column='DT_LIMITE', blank=True, null=True)
    # Field name made lowercase.
    evento = models.CharField(
        db_column='EVENTO', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(db_column='DT_INCLUSAO')
    # Field name made lowercase.
    arquivo = models.CharField(
        db_column='ARQUIVO', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2)
    # Field name made lowercase.
    municipio = models.IntegerField(
        db_column='MUNICIPIO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMAILS_BLOQUEADOS_PROCON'


class EmailHistoricoAlteracao(models.Model):
    # Field name made lowercase.
    contatos_id = models.CharField(
        db_column='CONTATOS_ID', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    email = models.CharField(
        db_column='EMAIL', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    prioridade = models.BigIntegerField(
        db_column='PRIORIDADE', blank=True, null=True)
    # Field name made lowercase.
    email_score = models.CharField(
        db_column='EMAIL_SCORE', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    email_pessoal = models.CharField(
        db_column='EMAIL_PESSOAL', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    email_duplicado = models.CharField(
        db_column='EMAIL_DUPLICADO', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    blacklist = models.CharField(
        db_column='BLACKLIST', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    estrutura = models.CharField(
        db_column='ESTRUTURA', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    status_vt = models.CharField(
        db_column='STATUS_VT', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    dominio = models.CharField(
        db_column='DOMINIO', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    mapas = models.IntegerField(db_column='MAPAS', blank=True, null=True)
    # Field name made lowercase.
    peso = models.IntegerField(db_column='PESO', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id = models.CharField(
        db_column='CADASTRO_ID', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)
    # Field name made lowercase.
    id_usuario_consultou = models.CharField(
        db_column='ID_USUARIO_CONSULTOU', max_length=1)
    # Field name made lowercase.
    dt_sci_data_consulta = models.CharField(
        db_column='DT_SCI_DATA_CONSULTA', max_length=1)
    # Field name made lowercase.
    dt_alteracao = models.CharField(db_column='DT_ALTERACAO', max_length=1)
    # Field name made lowercase.
    id_usuario = models.CharField(db_column='ID_USUARIO', max_length=1)
    # Field name made lowercase.
    ic_operacao = models.CharField(db_column='IC_OPERACAO', max_length=1)
    # Field name made lowercase. Field renamed because of name conflict.
    contatos_id_0 = models.BigIntegerField(
        db_column='CONTATOS_ID', blank=True, null=True)
    # Field name made lowercase. Field renamed because of name conflict.
    email_0 = models.CharField(
        db_column='EMAIL', max_length=255, blank=True, null=True)
    # Field name made lowercase. Field renamed because of name conflict.
    prioridade_0 = models.BigIntegerField(
        db_column='PRIORIDADE', blank=True, null=True)
    # Field name made lowercase. Field renamed because of name conflict.
    email_score_0 = models.CharField(
        db_column='EMAIL_SCORE', max_length=20, blank=True, null=True)
    # Field name made lowercase. Field renamed because of name conflict.
    email_pessoal_0 = models.CharField(
        db_column='EMAIL_PESSOAL', max_length=1, blank=True, null=True)
    # Field name made lowercase. Field renamed because of name conflict.
    email_duplicado_0 = models.CharField(
        db_column='EMAIL_DUPLICADO', max_length=1, blank=True, null=True)
    # Field name made lowercase. Field renamed because of name conflict.
    blacklist_0 = models.CharField(
        db_column='BLACKLIST', max_length=1, blank=True, null=True)
    # Field name made lowercase. Field renamed because of name conflict.
    estrutura_0 = models.CharField(
        db_column='ESTRUTURA', max_length=20, blank=True, null=True)
    # Field name made lowercase. Field renamed because of name conflict.
    status_vt_0 = models.CharField(
        db_column='STATUS_VT', max_length=20, blank=True, null=True)
    # Field name made lowercase. Field renamed because of name conflict.
    dominio_0 = models.CharField(
        db_column='DOMINIO', max_length=20, blank=True, null=True)
    # Field name made lowercase. Field renamed because of name conflict.
    mapas_0 = models.IntegerField(db_column='MAPAS', blank=True, null=True)
    # Field name made lowercase. Field renamed because of name conflict.
    peso_0 = models.IntegerField(db_column='PESO', blank=True, null=True)
    # Field name made lowercase. Field renamed because of name conflict.
    cadastro_id_0 = models.CharField(
        db_column='CADASTRO_ID', max_length=255, blank=True, null=True)
    # Field name made lowercase. Field renamed because of name conflict.
    dt_inclusao_0 = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)
    # Field name made lowercase.
    email_procon = models.CharField(
        db_column='EMAIL_PROCON', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    origem_dado_topdados = models.CharField(
        db_column='ORIGEM_DADO_TOPDADOS', max_length=100)
    # Field name made lowercase. Field renamed because of name conflict.
    id_usuario_consultou_0 = models.IntegerField(
        db_column='ID_USUARIO_CONSULTOU', blank=True, null=True)
    # Field name made lowercase. Field renamed because of name conflict.
    dt_sci_data_consulta_0 = models.DateTimeField(
        db_column='DT_SCI_DATA_CONSULTA', blank=True, null=True)
    # Field name made lowercase. Field renamed because of name conflict.
    dt_alteracao_0 = models.DateTimeField(
        db_column='DT_ALTERACAO', blank=True, null=True)
    # Field name made lowercase. Field renamed because of name conflict.
    id_usuario_0 = models.IntegerField(
        db_column='ID_USUARIO', blank=True, null=True)
    # Field name made lowercase. Field renamed because of name conflict.
    ic_operacao_0 = models.CharField(
        db_column='IC_OPERACAO', max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMAIL_HISTORICO_ALTERACAO'


class EmailPesoDescricao(models.Model):
    peso = models.IntegerField(db_column='PESO')  # Field name made lowercase.
    # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=200)

    class Meta:
        managed = False
        db_table = 'EMAIL_PESO_DESCRICAO'


class Empresas(models.Model):
    # Field name made lowercase.
    empresas_id = models.IntegerField(db_column='EMPRESAS_ID')
    # Field name made lowercase.
    cnpj = models.CharField(
        db_column='CNPJ', max_length=14, blank=True, null=True)
    # Field name made lowercase.
    cnpj_nota = models.IntegerField(
        db_column='CNPJ_NOTA', blank=True, null=True)
    # Field name made lowercase.
    razao_social = models.CharField(
        db_column='RAZAO_SOCIAL', max_length=155, blank=True, null=True)
    # Field name made lowercase.
    nome_mc = models.CharField(
        db_column='NOME_MC', max_length=35, blank=True, null=True)
    # Field name made lowercase.
    nome_nota = models.IntegerField(
        db_column='NOME_NOTA', blank=True, null=True)
    # Field name made lowercase.
    nome_fantasia = models.CharField(
        db_column='NOME_FANTASIA', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    nome_fantasia_mc = models.CharField(
        db_column='NOME_FANTASIA_MC', max_length=35, blank=True, null=True)
    # Field name made lowercase.
    data_fundacao = models.DateTimeField(
        db_column='DATA_FUNDACAO', blank=True, null=True)
    # Field name made lowercase.
    endereco = models.CharField(
        db_column='ENDERECO', max_length=130, blank=True, null=True)
    # Field name made lowercase.
    logr_tipo = models.CharField(
        db_column='LOGR_TIPO', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    logr_titulo = models.CharField(
        db_column='LOGR_TITULO', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    logr_nome = models.CharField(
        db_column='LOGR_NOME', max_length=70, blank=True, null=True)
    # Field name made lowercase.
    logr_numero = models.CharField(
        db_column='LOGR_NUMERO', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    logr_complemento = models.CharField(
        db_column='LOGR_COMPLEMENTO', max_length=70, blank=True, null=True)
    # Field name made lowercase.
    bairro = models.CharField(
        db_column='BAIRRO', max_length=40, blank=True, null=True)
    # Field name made lowercase.
    cidade = models.CharField(
        db_column='CIDADE', max_length=40, blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=8,
                           blank=True, null=True)
    # Field name made lowercase.
    cep_nota = models.IntegerField(db_column='CEP_NOTA', blank=True, null=True)
    # Field name made lowercase.
    match_end = models.CharField(
        db_column='MATCH_END', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    cod_ibge = models.CharField(
        db_column='COD_IBGE', max_length=7, blank=True, null=True)
    # Field name made lowercase.
    latitude = models.DecimalField(
        db_column='LATITUDE', max_digits=20, decimal_places=15, blank=True, null=True)
    # Field name made lowercase.
    longitude = models.DecimalField(
        db_column='LONGITUDE', max_digits=20, decimal_places=15, blank=True, null=True)
    # Field name made lowercase.
    cod_setor = models.CharField(
        db_column='COD_SETOR', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    status_geo = models.CharField(
        db_column='STATUS_GEO', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    match_geo = models.CharField(
        db_column='MATCH_GEO', max_length=32, blank=True, null=True)
    # Field name made lowercase.
    nat_juridi = models.IntegerField(
        db_column='NAT_JURIDI', blank=True, null=True)
    # Field name made lowercase.
    cnae = models.CharField(
        db_column='CNAE', max_length=5, blank=True, null=True)
    # Field name made lowercase.
    cnae_sg = models.CharField(
        db_column='CNAE_SG', max_length=7, blank=True, null=True)
    # Field name made lowercase.
    cod_sit_cad = models.SmallIntegerField(
        db_column='COD_SIT_CAD', blank=True, null=True)
    # Field name made lowercase.
    data_situacao_cadastral = models.DateTimeField(
        db_column='DATA_SITUACAO_CADASTRAL', blank=True, null=True)
    motivo_situacao_cadastral = models.SmallIntegerField(
        db_column='MOTIVO_SITUACAO_CADASTRAL', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    situacao_especial = models.SmallIntegerField(
        db_column='SITUACAO_ESPECIAL', blank=True, null=True)
    # Field name made lowercase.
    data_situacao_especial = models.DateTimeField(
        db_column='DATA_SITUACAO_ESPECIAL', blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)
    # Field name made lowercase.
    dt_alteracao = models.DateTimeField(
        db_column='DT_ALTERACAO', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id = models.IntegerField(
        db_column='CADASTRO_ID', blank=True, null=True)
    # Field name made lowercase.
    matriz = models.BooleanField(db_column='MATRIZ', blank=True, null=True)
    # Field name made lowercase.
    fx_fat = models.SmallIntegerField(
        db_column='FX_FAT', blank=True, null=True)
    # Field name made lowercase.
    fx_func = models.SmallIntegerField(
        db_column='FX_FUNC', blank=True, null=True)
    # Field name made lowercase.
    qtde_func = models.SmallIntegerField(
        db_column='QTDE_FUNC', blank=True, null=True)
    # Field name made lowercase.
    qtde_func_segmento = models.SmallIntegerField(
        db_column='QTDE_FUNC_SEGMENTO', blank=True, null=True)
    # Field name made lowercase.
    porte = models.SmallIntegerField(db_column='PORTE', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id_porte = models.IntegerField(
        db_column='CADASTRO_ID_PORTE', blank=True, null=True)
    # Field name made lowercase.
    data_opcao_simei = models.DateTimeField(
        db_column='DATA_OPCAO_SIMEI', blank=True, null=True)
    # Field name made lowercase.
    data_consulta = models.DateTimeField(
        db_column='DATA_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    hora_consulta = models.CharField(
        db_column='HORA_CONSULTA', max_length=8, blank=True, null=True)
    # Field name made lowercase.
    nota = models.IntegerField(db_column='NOTA', blank=True, null=True)
    contatos_id_repr_legal = models.BigIntegerField(
        db_column='CONTATOS_ID_REPR_LEGAL', blank=True, null=True)  # Field name made lowercase.
    data_consulta_repr_legal = models.DateTimeField(
        db_column='DATA_CONSULTA_REPR_LEGAL', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    hora_consulta_repr_legal = models.CharField(
        db_column='HORA_CONSULTA_REPR_LEGAL', max_length=8, blank=True, null=True)
    # Field name made lowercase.
    cadastro_id_repr_legal = models.IntegerField(
        db_column='CADASTRO_ID_REPR_LEGAL', blank=True, null=True)
    # Field name made lowercase.
    pre_screen = models.IntegerField(
        db_column='PRE_SCREEN', blank=True, null=True)
    # Field name made lowercase.
    pre_screen_in = models.FloatField(
        db_column='PRE_SCREEN_IN', blank=True, null=True)
    # Field name made lowercase.
    vl_fat_pre = models.IntegerField(
        db_column='VL_FAT_PRE', blank=True, null=True)
    # Field name made lowercase.
    dt_alteracao_vl_fat_pre = models.DateTimeField(
        db_column='DT_ALTERACAO_VL_FAT_PRE', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id_fat_pre = models.IntegerField(
        db_column='CADASTRO_ID_FAT_PRE', blank=True, null=True)
    # Field name made lowercase.
    cl_risco = models.CharField(
        db_column='CL_RISCO', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    tipo = models.CharField(
        db_column='TIPO', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    tipo_cnae = models.CharField(
        db_column='TIPO_CNAE', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    status = models.CharField(
        db_column='STATUS', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    dt_informacao = models.DateTimeField(
        db_column='DT_INFORMACAO', blank=True, null=True)
    # Field name made lowercase.
    fonte_recno_id = models.IntegerField(
        db_column='FONTE_RECNO_ID', blank=True, null=True)
    # Field name made lowercase.
    fonte_name = models.CharField(
        db_column='FONTE_NAME', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    inibir = models.SmallIntegerField(
        db_column='INIBIR', blank=True, null=True)
    # Field name made lowercase.
    socio_ambiental = models.SmallIntegerField(
        db_column='SOCIO_AMBIENTAL', blank=True, null=True)
    # Field name made lowercase.
    cod_ind_operacionalidade = models.IntegerField(
        db_column='COD_IND_OPERACIONALIDADE', blank=True, null=True)
    # Field name made lowercase.
    descr_ind_operacionalidade = models.CharField(
        db_column='DESCR_IND_OPERACIONALIDADE', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    ente_federativo_responsavel = models.CharField(
        db_column='ENTE_FEDERATIVO_RESPONSAVEL', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    capital_social = models.DecimalField(
        db_column='CAPITAL_SOCIAL', max_digits=13, decimal_places=0, blank=True, null=True)
    # Field name made lowercase.
    mosaic_business = models.CharField(
        db_column='MOSAIC_BUSINESS', max_length=3, blank=True, null=True)
    # Field name made lowercase.
    porte_receita = models.CharField(
        db_column='PORTE_RECEITA', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    pre_screening = models.FloatField(
        db_column='PRE_SCREENING', blank=True, null=True)
    # Field name made lowercase.
    risco = models.CharField(
        db_column='RISCO', max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMPRESAS'


class EmpresasAtualizaFilialQuality(models.Model):
    # Field name made lowercase.
    empresas_id = models.BigIntegerField(
        db_column='Empresas_ID', blank=True, null=True)
    # Field name made lowercase.
    matriz = models.IntegerField(db_column='Matriz', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMPRESAS_ATUALIZA_FILIAL_QUALITY'


class EmpresasCnae(models.Model):
    # Field name made lowercase.
    cnae_secao = models.CharField(
        db_column='CNAE_SECAO', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    cnae_divisao = models.CharField(
        db_column='CNAE_DIVISAO', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    cnae_grupo = models.CharField(
        db_column='CNAE_GRUPO', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    cnae_classe = models.CharField(
        db_column='CNAE_CLASSE', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    cnae_subclasse = models.CharField(
        db_column='CNAE_SUBCLASSE', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    cnae_descricao = models.CharField(
        db_column='CNAE_DESCRICAO', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    cnae_nivel = models.CharField(
        db_column='CNAE_NIVEL', max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMPRESAS_CNAE'


class EmpresasCnaeSecundario(models.Model):
    # Field name made lowercase.
    empresas_id = models.IntegerField(db_column='EMPRESAS_ID')
    # Field name made lowercase.
    cnae_subclasse = models.CharField(db_column='CNAE_SUBCLASSE', max_length=7)

    class Meta:
        managed = False
        db_table = 'EMPRESAS_CNAE_SECUNDARIO'


class EmpresasDadosReceita(models.Model):
    # Field name made lowercase.
    empresas_id = models.IntegerField(db_column='EMPRESAS_ID', unique=True)
    # Field name made lowercase.
    razao_social = models.CharField(
        db_column='RAZAO_SOCIAL', max_length=155, blank=True, null=True)
    # Field name made lowercase.
    nome_fantasia = models.CharField(
        db_column='NOME_FANTASIA', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    endereco = models.CharField(
        db_column='ENDERECO', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    logr_numero = models.CharField(
        db_column='LOGR_NUMERO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    logr_complemento = models.CharField(
        db_column='LOGR_COMPLEMENTO', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    bairro = models.CharField(
        db_column='BAIRRO', max_length=70, blank=True, null=True)
    # Field name made lowercase.
    cidade = models.CharField(
        db_column='CIDADE', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=8,
                           blank=True, null=True)
    # Field name made lowercase.
    cod_ibge = models.CharField(
        db_column='COD_IBGE', max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMPRESAS_DADOS_RECEITA'


class EmpresasEmail(models.Model):
    # Field name made lowercase.
    empresas_id = models.BigIntegerField(
        db_column='EMPRESAS_ID', blank=True, null=True)
    # Field name made lowercase.
    email = models.CharField(
        db_column='EMAIL', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    cadastro_id = models.CharField(
        db_column='CADASTRO_ID', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)
    # Field name made lowercase.
    situacao = models.CharField(
        db_column='SITUACAO', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    dominio = models.CharField(
        db_column='DOMINIO', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    peso = models.SmallIntegerField(db_column='PESO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMPRESAS_EMAIL'


class EmpresasEnderecos(models.Model):
    # Field name made lowercase.
    endereco_empresas_id = models.BigIntegerField(
        db_column='ENDERECO_EMPRESAS_ID', blank=True, null=True)
    # Field name made lowercase.
    cnpj = models.CharField(
        db_column='CNPJ', max_length=14, blank=True, null=True)
    # Field name made lowercase.
    endereco = models.CharField(
        db_column='ENDERECO', max_length=903, blank=True, null=True)
    # Field name made lowercase.
    bairro = models.CharField(
        db_column='BAIRRO', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    cep = models.CharField(
        db_column='CEP', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    cidade = models.CharField(
        db_column='CIDADE', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    estado = models.CharField(
        db_column='ESTADO', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(db_column='DT_INCLUSAO')
    # Field name made lowercase.
    dt_atualizacao = models.IntegerField(
        db_column='DT_ATUALIZACAO', blank=True, null=True)
    # Field name made lowercase.
    origem = models.CharField(db_column='ORIGEM', max_length=6)

    class Meta:
        managed = False
        db_table = 'EMPRESAS_ENDERECOS'


class EmpresasHistoricoSintegra(models.Model):
    # Field name made lowercase.
    empresas_id = models.IntegerField(db_column='EMPRESAS_ID')
    # Field name made lowercase.
    inscricao_estadual = models.CharField(
        db_column='INSCRICAO_ESTADUAL', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    razao_social = models.CharField(
        db_column='RAZAO_SOCIAL', max_length=155, blank=True, null=True)
    # Field name made lowercase.
    endereco = models.CharField(
        db_column='ENDERECO', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    numero = models.CharField(
        db_column='NUMERO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    logr_complemento = models.CharField(
        db_column='LOGR_COMPLEMENTO', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    bairro = models.CharField(
        db_column='BAIRRO', max_length=70, blank=True, null=True)
    # Field name made lowercase.
    cidade = models.CharField(
        db_column='CIDADE', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    cep = models.CharField(
        db_column='CEP', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    telefone = models.CharField(
        db_column='TELEFONE', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    atividade_economica = models.TextField(
        db_column='ATIVIDADE_ECONOMICA', blank=True, null=True)
    # Field name made lowercase.
    atividade_secundaria = models.TextField(
        db_column='ATIVIDADE_SECUNDARIA', blank=True, null=True)
    # Field name made lowercase.
    data_inicio_atividade = models.CharField(
        db_column='DATA_INICIO_ATIVIDADE', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    data_fim_atividade = models.CharField(
        db_column='DATA_FIM_ATIVIDADE', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    situacao_cadastral = models.CharField(
        db_column='SITUACAO_CADASTRAL', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    data_situacao_cadastral = models.CharField(
        db_column='DATA_SITUACAO_CADASTRAL', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    data_consulta = models.CharField(
        db_column='DATA_CONSULTA', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    numero_consulta = models.CharField(
        db_column='NUMERO_CONSULTA', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    sit_cad_padronizada = models.CharField(
        db_column='SIT_CAD_PADRONIZADA', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    data_inicio_tratada = models.DateTimeField(
        db_column='DATA_INICIO_TRATADA', blank=True, null=True)
    # Field name made lowercase.
    data_consulta_tratada = models.DateTimeField(
        db_column='DATA_CONSULTA_TRATADA', blank=True, null=True)
    # Field name made lowercase.
    data_situacao_tratada = models.DateTimeField(
        db_column='DATA_SITUACAO_TRATADA', blank=True, null=True)
    # Field name made lowercase.
    dt_atualizacao = models.DateTimeField(
        db_column='DT_ATUALIZACAO', blank=True, null=True)
    # Field name made lowercase.
    excluido = models.BooleanField(db_column='EXCLUIDO')
    # Field name made lowercase.
    origem = models.CharField(
        db_column='ORIGEM', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    vrf = models.CharField(db_column='VRF', max_length=2,
                           blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMPRESAS_HISTORICO_SINTEGRA'


class EmpresasHistoricoSuframa(models.Model):
    # Field name made lowercase.
    empresas_id = models.IntegerField(
        db_column='EMPRESAS_ID', blank=True, null=True)
    # Field name made lowercase.
    inscricao_suframa = models.CharField(
        db_column='INSCRICAO_SUFRAMA', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    data_inscricao_suframa = models.CharField(
        db_column='DATA_INSCRICAO_SUFRAMA', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    situacao_cadastral = models.CharField(
        db_column='SITUACAO_CADASTRAL', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    data_validade = models.CharField(
        db_column='DATA_VALIDADE', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    tipo_incentivo = models.CharField(
        db_column='TIPO_INCENTIVO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    isenta_tsa = models.CharField(
        db_column='ISENTA_TSA', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    data_consulta = models.DateTimeField(
        db_column='DATA_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    mensagem_suframa = models.CharField(
        db_column='MENSAGEM_SUFRAMA', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMPRESAS_HISTORICO_SUFRAMA'
        unique_together = (('empresas_id', 'inscricao_suframa'),)


class EmpresasNaturezaJuridica(models.Model):
    # Field name made lowercase.
    cod_nat_jur = models.IntegerField(
        db_column='COD_NAT_JUR', db_comment='- C¾digo da Natureza JurÝdica ')
    # Field name made lowercase.
    desc_nat_jur = models.CharField(db_column='DESC_NAT_JUR', max_length=200,
                                    blank=True, null=True, db_comment='- DescriþÒo da Natureza JurÝdi')

    class Meta:
        managed = False
        db_table = 'EMPRESAS_NATUREZA_JURIDICA'


class EmpresasPorte(models.Model):
    # Field name made lowercase.
    fx_porte = models.SmallIntegerField(db_column='FX_PORTE')
    # Field name made lowercase.
    ds_porte = models.CharField(db_column='DS_PORTE', max_length=40)

    class Meta:
        managed = False
        db_table = 'EMPRESAS_PORTE'


class EmpresasReceitaCnae(models.Model):
    # Field name made lowercase.
    cnae = models.CharField(
        db_column='CNAE', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    cnae_descricao = models.CharField(
        db_column='CNAE_DESCRICAO', max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMPRESAS_RECEITA_CNAE'


class EmpresasReceitaEmpresas(models.Model):
    # Field name made lowercase.
    cnpj_basico = models.CharField(
        db_column='CNPJ_BASICO', max_length=8, blank=True, null=True)
    # Field name made lowercase.
    razao_social = models.CharField(
        db_column='RAZAO_SOCIAL', max_length=1000, blank=True, null=True)
    # Field name made lowercase.
    natureza_juridica = models.CharField(
        db_column='NATUREZA_JURIDICA', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    qualificacao_responsavel = models.CharField(
        db_column='QUALIFICACAO_RESPONSAVEL', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    capital_social = models.CharField(
        db_column='CAPITAL_SOCIAL', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    porte = models.CharField(
        db_column='PORTE', max_length=5, blank=True, null=True)
    # Field name made lowercase.
    ente_federativo = models.CharField(
        db_column='ENTE_FEDERATIVO', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMPRESAS_RECEITA_EMPRESAS'


class EmpresasReceitaEstabelecimento(models.Model):
    # Field name made lowercase.
    cnpj_basico = models.CharField(
        db_column='CNPJ_BASICO', max_length=8, blank=True, null=True)
    # Field name made lowercase.
    cnpj_ordem = models.CharField(
        db_column='CNPJ_ORDEM', max_length=4, blank=True, null=True)
    # Field name made lowercase.
    cnpj_dv = models.CharField(
        db_column='CNPJ_DV', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    matriz_filial = models.CharField(
        db_column='MATRIZ_FILIAL', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    nome_fantasia = models.CharField(
        db_column='NOME_FANTASIA', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    situacao_cadastral = models.CharField(
        db_column='SITUACAO_CADASTRAL', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    data_situacao_cadastral = models.CharField(
        db_column='DATA_SITUACAO_CADASTRAL', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    motivo_situacao = models.CharField(
        db_column='MOTIVO_SITUACAO', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    nome_cidade_exterior = models.CharField(
        db_column='NOME_CIDADE_EXTERIOR', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    pais = models.CharField(
        db_column='PAIS', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    data_inicio_atividade = models.CharField(
        db_column='DATA_INICIO_ATIVIDADE', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    cnae_principal = models.CharField(
        db_column='CNAE_PRINCIPAL', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    cnae_fiscal = models.CharField(
        db_column='CNAE_FISCAL', max_length=4000, blank=True, null=True)
    # Field name made lowercase.
    tipo_logradouro = models.CharField(
        db_column='TIPO_LOGRADOURO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    logradouro = models.CharField(
        db_column='LOGRADOURO', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    numero = models.CharField(
        db_column='NUMERO', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    complemento = models.CharField(
        db_column='COMPLEMENTO', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    bairro = models.CharField(
        db_column='BAIRRO', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    cep = models.CharField(
        db_column='CEP', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    municipio = models.CharField(
        db_column='MUNICIPIO', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    ddd1 = models.CharField(
        db_column='DDD1', max_length=5, blank=True, null=True)
    # Field name made lowercase.
    telefone1 = models.CharField(
        db_column='TELEFONE1', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    ddd2 = models.CharField(
        db_column='DDD2', max_length=5, blank=True, null=True)
    # Field name made lowercase.
    telefone2 = models.CharField(
        db_column='TELEFONE2', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    ddd3 = models.CharField(
        db_column='DDD3', max_length=5, blank=True, null=True)
    # Field name made lowercase.
    telefone3 = models.CharField(
        db_column='TELEFONE3', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    email = models.CharField(
        db_column='EMAIL', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    situacao_especial = models.CharField(
        db_column='SITUACAO_ESPECIAL', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    data_situacao_especial = models.CharField(
        db_column='DATA_SITUACAO_ESPECIAL', max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMPRESAS_RECEITA_ESTABELECIMENTO'


class EmpresasReceitaMunicipio(models.Model):
    # Field name made lowercase.
    cd_municipio = models.CharField(
        db_column='CD_MUNICIPIO', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    municipio = models.CharField(
        db_column='MUNICIPIO', max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMPRESAS_RECEITA_MUNICIPIO'


class EmpresasReceitaNaturezaJuridica(models.Model):
    # Field name made lowercase.
    cd_natureza_juridica = models.CharField(
        db_column='CD_NATUREZA_JURIDICA', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    natureza_juridica = models.CharField(
        db_column='NATUREZA_JURIDICA', max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMPRESAS_RECEITA_NATUREZA_JURIDICA'


class EmpresasReceitaPaises(models.Model):
    # Field name made lowercase.
    cd_pais = models.CharField(
        db_column='CD_PAIS', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    pais = models.CharField(
        db_column='PAIS', max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMPRESAS_RECEITA_PAISES'


class EmpresasReceitaQualificacaoSocio(models.Model):
    # Field name made lowercase.
    cd_qualificacao_socio = models.CharField(
        db_column='CD_QUALIFICACAO_SOCIO', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    qualificacao_socio = models.CharField(
        db_column='QUALIFICACAO_SOCIO', max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMPRESAS_RECEITA_QUALIFICACAO_SOCIO'


class EmpresasReceitaSimples(models.Model):
    # Field name made lowercase.
    cnpj_basico = models.CharField(
        db_column='CNPJ_BASICO', max_length=8, blank=True, null=True)
    # Field name made lowercase.
    opcao_simples = models.CharField(
        db_column='OPCAO_SIMPLES', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    data_opcao_simples = models.CharField(
        db_column='DATA_OPCAO_SIMPLES', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    data_exclusao_simples = models.CharField(
        db_column='DATA_EXCLUSAO_SIMPLES', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    opcao_me = models.CharField(
        db_column='OPCAO_ME', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    data_opcao_mei = models.CharField(
        db_column='DATA_OPCAO_MEI', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    data_exclusao_mei = models.CharField(
        db_column='DATA_EXCLUSAO_MEI', max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMPRESAS_RECEITA_SIMPLES'


class EmpresasReceitaSituacaoCadastral(models.Model):
    # Field name made lowercase.
    cd_situacao_cadastral = models.CharField(
        db_column='CD_SITUACAO_CADASTRAL', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    situacao_cadastral = models.CharField(
        db_column='SITUACAO_CADASTRAL', max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMPRESAS_RECEITA_SITUACAO_CADASTRAL'


class EmpresasReceitaSocios(models.Model):
    # Field name made lowercase.
    cnpj_basico = models.CharField(
        db_column='CNPJ_BASICO', max_length=8, blank=True, null=True)
    # Field name made lowercase.
    identificador_socio = models.CharField(
        db_column='IDENTIFICADOR_SOCIO', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    nome_socio = models.CharField(
        db_column='NOME_SOCIO', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    cpf_cnpj = models.CharField(
        db_column='CPF_CNPJ', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    qualificacao_socio = models.CharField(
        db_column='QUALIFICACAO_SOCIO', max_length=5, blank=True, null=True)
    # Field name made lowercase.
    data_entrada_sociedade = models.CharField(
        db_column='DATA_ENTRADA_SOCIEDADE', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    pais = models.CharField(
        db_column='PAIS', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    representante_legal = models.CharField(
        db_column='REPRESENTANTE_LEGAL', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    nome_representante = models.CharField(
        db_column='NOME_REPRESENTANTE', max_length=300, blank=True, null=True)
    qualificacao_representante_legal = models.CharField(
        db_column='QUALIFICACAO_REPRESENTANTE_LEGAL', max_length=5, blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    faixa_etaria = models.CharField(
        db_column='FAIXA_ETARIA', max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMPRESAS_RECEITA_SOCIOS'


class EmpresasSimplesNacional(models.Model):
    # Field name made lowercase.
    empresas_id = models.BigIntegerField(
        db_column='EMPRESAS_ID', primary_key=True, blank=True, null=True)
    # Field name made lowercase.
    cnpj = models.CharField(
        db_column='CNPJ', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    opcao_simei = models.CharField(
        db_column='OPCAO_SIMEI', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    dt_simei = models.DateTimeField(
        db_column='DT_SIMEI', blank=True, null=True)
    # Field name made lowercase.
    opcao_simples = models.CharField(
        db_column='OPCAO_SIMPLES', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    dt_simples = models.DateTimeField(
        db_column='DT_SIMPLES', blank=True, null=True)
    # Field name made lowercase.
    dt_info_simples = models.DateTimeField(
        db_column='DT_INFO_SIMPLES', blank=True, null=True)
    # Field name made lowercase. Field renamed because of name conflict.
    empresas_id_0 = models.BigIntegerField(
        db_column='EMPRESAS_ID', primary_key=True)
    # Field name made lowercase.
    status_simples = models.CharField(db_column='STATUS_SIMPLES', max_length=1)
    # Field name made lowercase.
    dt_consulta = models.DateTimeField(db_column='DT_CONSULTA')
    # Field name made lowercase.
    status_simei = models.CharField(db_column='STATUS_SIMEI', max_length=1)
    # Field name made lowercase.
    dt_opcao_simples = models.DateTimeField(
        db_column='DT_OPCAO_SIMPLES', blank=True, null=True)
    # Field name made lowercase.
    dt_opcao_simei = models.DateTimeField(
        db_column='DT_OPCAO_SIMEI', blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)
    # Field name made lowercase.
    dt_alteracao = models.DateTimeField(
        db_column='DT_ALTERACAO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMPRESAS_SIMPLES_NACIONAL'


class EmpresasSituacaoCadastral(models.Model):
    # Field name made lowercase.
    id_sit_cad = models.SmallIntegerField(
        db_column='ID_SIT_CAD', db_comment='- C¾digo Sequencial Interno da')
    # Field name made lowercase.
    desc_sit_cad = models.CharField(db_column='DESC_SIT_CAD', max_length=100,
                                    blank=True, null=True, db_comment='- Nome da SituaþÒo Cadastral d')
    # Field name made lowercase.
    cod_sit_cad = models.IntegerField(
        db_column='COD_SIT_CAD', blank=True, null=True, db_comment='- C¾digo da SituaþÒo Cadastral')

    class Meta:
        managed = False
        db_table = 'EMPRESAS_SITUACAO_CADASTRAL'


class EmpresasSocios(models.Model):
    # Field name made lowercase.
    empresas_id = models.IntegerField(
        db_column='EMPRESAS_ID', blank=True, null=True)
    # Field name made lowercase.
    tp_socio_id = models.SmallIntegerField(
        db_column='TP_SOCIO_ID', blank=True, null=True)
    # Field name made lowercase.
    empresas_id_socio = models.IntegerField(
        db_column='EMPRESAS_ID_SOCIO', blank=True, null=True)
    # Field name made lowercase.
    contatos_id_socio = models.IntegerField(
        db_column='CONTATOS_ID_SOCIO', blank=True, null=True)
    # Field name made lowercase.
    participacao_socio = models.DecimalField(
        db_column='PARTICIPACAO_SOCIO', max_digits=5, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    nr_seq = models.IntegerField(db_column='NR_SEQ')

    class Meta:
        managed = False
        db_table = 'EMPRESAS_SOCIOS'


class EmpresasSociosInvalidos(models.Model):
    # Field name made lowercase.
    empresas_id = models.IntegerField(
        db_column='EMPRESAS_ID', blank=True, null=True)
    # Field name made lowercase.
    tp_socio = models.ForeignKey(
        'TipoSocio', models.DO_NOTHING, db_column='TP_SOCIO_ID', blank=True, null=True)
    # Field name made lowercase.
    nome_empresa_socio = models.CharField(
        db_column='NOME_EMPRESA_SOCIO', max_length=70, blank=True, null=True)
    # Field name made lowercase.
    nome_contato_socio = models.CharField(
        db_column='NOME_CONTATO_SOCIO', max_length=70, blank=True, null=True)
    # Field name made lowercase.
    participacao_socio = models.DecimalField(
        db_column='PARTICIPACAO_SOCIO', max_digits=5, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    nr_seq = models.IntegerField(db_column='NR_SEQ')

    class Meta:
        managed = False
        db_table = 'EMPRESAS_SOCIOS_INVALIDOS'


class EmpresasTelefone(models.Model):
    # Field name made lowercase.
    empresas_h_telefones_id = models.BigIntegerField(
        db_column='EMPRESAS_H_TELEFONES_ID')
    # Field name made lowercase.
    empresas_id = models.BigIntegerField(db_column='EMPRESAS_ID')
    # Field name made lowercase.
    ddd = models.CharField(db_column='DDD', max_length=2,
                           blank=True, null=True)
    # Field name made lowercase.
    telefone = models.CharField(
        db_column='TELEFONE', max_length=9, blank=True, null=True)
    # Field name made lowercase.
    tipo_telefone = models.SmallIntegerField(
        db_column='TIPO_TELEFONE', blank=True, null=True)
    # Field name made lowercase.
    fone_nota = models.SmallIntegerField(
        db_column='FONE_NOTA', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id = models.IntegerField(db_column='CADASTRO_ID')
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)
    # Field name made lowercase.
    dt_atualizacao = models.DateTimeField(
        db_column='DT_ATUALIZACAO', blank=True, null=True)
    # Field name made lowercase.
    dt_informacao = models.DateTimeField(
        db_column='DT_INFORMACAO', blank=True, null=True)
    # Field name made lowercase.
    origem_serasa = models.CharField(
        db_column='ORIGEM_SERASA', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    nsu = models.CharField(
        db_column='NSU', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    status = models.SmallIntegerField(
        db_column='STATUS', blank=True, null=True)
    # Field name made lowercase.
    prioridade = models.IntegerField(
        db_column='PRIORIDADE', blank=True, null=True)
    # Field name made lowercase.
    classificacao = models.CharField(
        db_column='CLASSIFICACAO', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    dt_metralhadora = models.DateTimeField(
        db_column='DT_METRALHADORA', blank=True, null=True)
    # Field name made lowercase.
    fonte_name = models.CharField(
        db_column='FONTE_NAME', max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMPRESAS_TELEFONE'


class EmpresaReceitaCpfPessoaFisica(models.Model):
    # Field name made lowercase.
    cpf = models.CharField(
        db_column='CPF', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    cpf_receita = models.CharField(
        db_column='CPF_RECEITA', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    nome = models.CharField(
        db_column='NOME', max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMPRESA_RECEITA_CPF_PESSOA_FISICA'


class Endereco(models.Model):
    # Field name made lowercase.
    historico_enderecos_id = models.BigIntegerField(
        db_column='HISTORICO_ENDERECOS_ID')
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    logr_tipo = models.CharField(
        db_column='LOGR_TIPO', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    logr_titulo = models.CharField(
        db_column='LOGR_TITULO', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    logr_nome = models.CharField(
        db_column='LOGR_NOME', max_length=60, blank=True, null=True)
    # Field name made lowercase.
    logr_numero = models.CharField(
        db_column='LOGR_NUMERO', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    logr_complemento = models.CharField(
        db_column='LOGR_COMPLEMENTO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    bairro = models.CharField(
        db_column='BAIRRO', max_length=40, blank=True, null=True)
    # Field name made lowercase.
    cidade = models.CharField(
        db_column='CIDADE', max_length=40, blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=8,
                           blank=True, null=True)
    # Field name made lowercase.
    match_end = models.CharField(
        db_column='MATCH_END', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    endereco = models.CharField(
        db_column='ENDERECO', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    cep_nota = models.IntegerField(db_column='CEP_NOTA', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id = models.IntegerField(
        db_column='CADASTRO_ID', blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)
    # Field name made lowercase.
    dt_atualizacao = models.DateTimeField(
        db_column='DT_ATUALIZACAO', blank=True, null=True)
    # Field name made lowercase.
    dt_informacao = models.DateTimeField(
        db_column='DT_INFORMACAO', blank=True, null=True)
    # Field name made lowercase.
    nsu = models.CharField(
        db_column='NSU', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    origem_srs = models.CharField(
        db_column='ORIGEM_SRS', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    latitude = models.DecimalField(
        db_column='LATITUDE', max_digits=20, decimal_places=15, blank=True, null=True)
    # Field name made lowercase.
    longitude = models.DecimalField(
        db_column='LONGITUDE', max_digits=20, decimal_places=15, blank=True, null=True)
    # Field name made lowercase.
    status_geo = models.CharField(
        db_column='STATUS_GEO', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    cod_setor = models.CharField(
        db_column='COD_SETOR', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    match_geo = models.CharField(
        db_column='MATCH_GEO', max_length=32, blank=True, null=True)
    # Field name made lowercase.
    tipo_endereco_id = models.SmallIntegerField(
        db_column='TIPO_ENDERECO_ID', blank=True, null=True)
    # Field name made lowercase.
    prioridade = models.IntegerField(
        db_column='PRIORIDADE', blank=True, null=True)
    # Field name made lowercase.
    classificacao = models.CharField(
        db_column='CLASSIFICACAO', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    fonte_name = models.CharField(
        db_column='FONTE_NAME', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    id_usuario_consultou = models.IntegerField(
        db_column='ID_USUARIO_CONSULTOU', blank=True, null=True)
    # Field name made lowercase.
    dt_sci_data_consulta = models.DateTimeField(
        db_column='DT_SCI_DATA_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    origem_dado_topdados = models.CharField(
        db_column='ORIGEM_DADO_TOPDADOS', max_length=100)
    dt_bigdata_data_consulta = models.DateTimeField(
        db_column='DT_BIGDATA_DATA_CONSULTA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ENDERECO'


class EnderecoHistoricoAlteracao(models.Model):
    # Field name made lowercase.
    historico_enderecos_id = models.BigIntegerField(
        db_column='HISTORICO_ENDERECOS_ID')
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    logr_tipo = models.CharField(
        db_column='LOGR_TIPO', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    logr_titulo = models.CharField(
        db_column='LOGR_TITULO', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    logr_nome = models.CharField(
        db_column='LOGR_NOME', max_length=60, blank=True, null=True)
    # Field name made lowercase.
    logr_numero = models.CharField(
        db_column='LOGR_NUMERO', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    logr_complemento = models.CharField(
        db_column='LOGR_COMPLEMENTO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    bairro = models.CharField(
        db_column='BAIRRO', max_length=40, blank=True, null=True)
    # Field name made lowercase.
    cidade = models.CharField(
        db_column='CIDADE', max_length=40, blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=8,
                           blank=True, null=True)
    # Field name made lowercase.
    match_end = models.CharField(
        db_column='MATCH_END', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    endereco = models.CharField(
        db_column='ENDERECO', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    cep_nota = models.IntegerField(db_column='CEP_NOTA', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id = models.IntegerField(
        db_column='CADASTRO_ID', blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)
    # Field name made lowercase.
    dt_atualizacao = models.DateTimeField(
        db_column='DT_ATUALIZACAO', blank=True, null=True)
    # Field name made lowercase.
    dt_informacao = models.DateTimeField(
        db_column='DT_INFORMACAO', blank=True, null=True)
    # Field name made lowercase.
    nsu = models.CharField(
        db_column='NSU', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    origem_srs = models.CharField(
        db_column='ORIGEM_SRS', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    latitude = models.DecimalField(
        db_column='LATITUDE', max_digits=20, decimal_places=15, blank=True, null=True)
    # Field name made lowercase.
    longitude = models.DecimalField(
        db_column='LONGITUDE', max_digits=20, decimal_places=15, blank=True, null=True)
    # Field name made lowercase.
    status_geo = models.CharField(
        db_column='STATUS_GEO', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    cod_setor = models.CharField(
        db_column='COD_SETOR', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    match_geo = models.CharField(
        db_column='MATCH_GEO', max_length=32, blank=True, null=True)
    # Field name made lowercase.
    tipo_endereco_id = models.SmallIntegerField(
        db_column='TIPO_ENDERECO_ID', blank=True, null=True)
    # Field name made lowercase.
    prioridade = models.IntegerField(
        db_column='PRIORIDADE', blank=True, null=True)
    # Field name made lowercase.
    classificacao = models.CharField(
        db_column='CLASSIFICACAO', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    fonte_name = models.CharField(
        db_column='FONTE_NAME', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    id_usuario_consultou = models.IntegerField(
        db_column='ID_USUARIO_CONSULTOU', blank=True, null=True)
    # Field name made lowercase.
    dt_sci_data_consulta = models.DateTimeField(
        db_column='DT_SCI_DATA_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    origem_dado_topdados = models.CharField(
        db_column='ORIGEM_DADO_TOPDADOS', max_length=100)
    # Field name made lowercase.
    dt_alteracao = models.DateTimeField(
        db_column='DT_ALTERACAO', blank=True, null=True)
    # Field name made lowercase.
    id_usuario = models.IntegerField(
        db_column='ID_USUARIO', blank=True, null=True)
    # Field name made lowercase.
    ic_operacao = models.CharField(db_column='IC_OPERACAO', max_length=1,
                                   blank=True, null=True, db_comment='A = AlteraþÒo / E = ExclusÒo')

    class Meta:
        managed = False
        db_table = 'ENDERECO_HISTORICO_ALTERACAO'


class EnderecoNovos(models.Model):
    # Field name made lowercase.
    endereco_novos_id = models.BigIntegerField(
        db_column='ENDERECO_NOVOS_ID', blank=True, null=True)
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    endereco = models.CharField(
        db_column='ENDERECO', max_length=400, blank=True, null=True)
    # Field name made lowercase.
    bairro = models.CharField(
        db_column='BAIRRO', max_length=40, blank=True, null=True)
    # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=8,
                           blank=True, null=True)
    # Field name made lowercase.
    cidade = models.CharField(
        db_column='CIDADE', max_length=40, blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    origem_dado_topdados = models.CharField(
        db_column='ORIGEM_DADO_TOPDADOS', max_length=100)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(db_column='DT_INCLUSAO')

    class Meta:
        managed = False
        db_table = 'ENDERECO_NOVOS'


class EnderecoNovosHistoricoAlteracao(models.Model):
    # Field name made lowercase.
    endereco_novos_id = models.BigIntegerField(
        db_column='ENDERECO_NOVOS_ID', blank=True, null=True)
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    endereco = models.CharField(
        db_column='ENDERECO', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    bairro = models.CharField(
        db_column='BAIRRO', max_length=40, blank=True, null=True)
    # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=8,
                           blank=True, null=True)
    # Field name made lowercase.
    cidade = models.CharField(
        db_column='CIDADE', max_length=40, blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    origem_dado_topdados = models.CharField(
        db_column='ORIGEM_DADO_TOPDADOS', max_length=100)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(db_column='DT_INCLUSAO')
    # Field name made lowercase.
    dt_alteracao = models.DateTimeField(
        db_column='DT_ALTERACAO', blank=True, null=True)
    # Field name made lowercase.
    id_usuario = models.IntegerField(
        db_column='ID_USUARIO', blank=True, null=True)
    # Field name made lowercase.
    ic_operacao = models.CharField(db_column='IC_OPERACAO', max_length=1,
                                   blank=True, null=True, db_comment='A = AlteraþÒo / E = ExclusÒo')

    class Meta:
        managed = False
        db_table = 'ENDERECO_NOVOS_HISTORICO_ALTERACAO'


class EstadoCivil(models.Model):
    # Field name made lowercase.
    estciv_id = models.SmallIntegerField(
        db_column='ESTCIV_ID', db_comment='- C¾digo Interno Sequencial do')
    # Field name made lowercase.
    estciv_sigla = models.CharField(db_column='ESTCIV_SIGLA', max_length=2,
                                    blank=True, null=True, db_comment='- Sigla do Estado Civil')
    # Field name made lowercase.
    estciv_descricao = models.CharField(
        db_column='ESTCIV_DESCRICAO', max_length=40, blank=True, null=True, db_comment='- Nome do Estado Civil')

    class Meta:
        managed = False
        db_table = 'ESTADO_CIVIL'


class ExpurgoRegiaoSulCreditTarget(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')

    class Meta:
        managed = False
        db_table = 'EXPURGO_REGIAO_SUL_CREDIT_TARGET'


class ExpurgoRegiaoSulCsb8(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')

    class Meta:
        managed = False
        db_table = 'EXPURGO_REGIAO_SUL_CSB8'


class FaixaFaturamento(models.Model):
    # Field name made lowercase.
    fx_fat = models.SmallAutoField(
        db_column='FX_FAT', primary_key=True, db_comment='*** DESCRIÃ├O AQUI ***')
    # Field name made lowercase.
    ds_fat = models.CharField(
        db_column='DS_FAT', max_length=40, db_comment='- Nome da Faixa do Faturamento')

    class Meta:
        managed = False
        db_table = 'FAIXA_FATURAMENTO'


class FaixaFuncionario(models.Model):
    # Field name made lowercase.
    id_func = models.SmallAutoField(
        db_column='ID_FUNC', primary_key=True, db_comment='- C¾digo Interno Sequencial da')
    # Field name made lowercase.
    ds_func = models.CharField(
        db_column='DS_FUNC', max_length=70, db_comment='*** DESCRIÃ├O AQUI ***')
    # Field name made lowercase.
    fx_func = models.SmallIntegerField(
        db_column='FX_FUNC', blank=True, null=True, db_comment='- Nome da Faixa do Funcionßrio')

    class Meta:
        managed = False
        db_table = 'FAIXA_FUNCIONARIO'


class FaixaRenda(models.Model):
    # Field name made lowercase.
    faixa_renda_id = models.AutoField(
        db_column='FAIXA_RENDA_ID', primary_key=True, db_comment='- C¾digo Interno Sequencial da')
    # Field name made lowercase.
    faixa_renda_descr = models.CharField(
        db_column='FAIXA_RENDA_DESCR', max_length=40, blank=True, null=True, db_comment='- Nome da Faixa de Renda')

    class Meta:
        managed = False
        db_table = 'FAIXA_RENDA'


class FaixaRendaHousehold(models.Model):
    faixa_renda_household_id = models.SmallIntegerField(
        db_column='FAIXA_RENDA_HOUSEHOLD_ID', primary_key=True)  # Field name made lowercase.
    # Field name made lowercase.
    faixa_renda_household_descr = models.CharField(
        db_column='FAIXA_RENDA_HOUSEHOLD_DESCR', max_length=40, blank=True, null=True)
    faixa_renda_household_vl_inicio = models.DecimalField(
        db_column='FAIXA_RENDA_HOUSEHOLD_VL_INICIO', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    faixa_renda_household_vl_final = models.DecimalField(
        db_column='FAIXA_RENDA_HOUSEHOLD_VL_FINAL', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FAIXA_RENDA_HOUSEHOLD'


class FaixaTriagemRiscoPj(models.Model):
    # Field name made lowercase.
    cl_risco = models.CharField(
        db_column='CL_RISCO', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    fx_risco = models.CharField(
        db_column='FX_RISCO', max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FAIXA_TRIAGEM_RISCO_PJ'


class HhExcluir(models.Model):
    # Field name made lowercase.
    household_id_2016 = models.IntegerField(db_column='HOUSEHOLD_ID_2016')
    # Field name made lowercase.
    match_end = models.CharField(
        db_column='MATCH_END', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    origem = models.CharField(db_column='ORIGEM', max_length=28)
    # Field name made lowercase.
    qtde_pessoas_household = models.IntegerField(
        db_column='QTDE_PESSOAS_HOUSEHOLD', blank=True, null=True)
    # Field name made lowercase.
    ddd = models.SmallIntegerField(db_column='DDD', blank=True, null=True)
    # Field name made lowercase.
    telefone = models.IntegerField(db_column='TELEFONE', blank=True, null=True)
    # Field name made lowercase.
    faixa_renda_household_id = models.IntegerField(
        db_column='FAIXA_RENDA_HOUSEHOLD_ID')

    class Meta:
        managed = False
        db_table = 'HH_EXCLUIR'


class HistoricoEnderecosMatch15(models.Model):
    # Field name made lowercase.
    match_end = models.CharField(
        db_column='Match_End', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    total = models.IntegerField(db_column='TOTAL', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HISTORICO_ENDERECOS_MATCH_15'


class HistoricoEnderecosPj(models.Model):
    # Field name made lowercase.
    historico_enderecos_id = models.BigAutoField(
        db_column='HISTORICO_ENDERECOS_ID', unique=True)
    # Field name made lowercase.
    empresas_id = models.BigIntegerField(db_column='EMPRESAS_ID')
    # Field name made lowercase.
    logr_tipo = models.CharField(
        db_column='LOGR_TIPO', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    logr_titulo = models.CharField(
        db_column='LOGR_TITULO', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    logr_nome = models.CharField(
        db_column='LOGR_NOME', max_length=70, blank=True, null=True)
    # Field name made lowercase.
    logr_numero = models.CharField(
        db_column='LOGR_NUMERO', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    logr_complemento = models.CharField(
        db_column='LOGR_COMPLEMENTO', max_length=70, blank=True, null=True)
    # Field name made lowercase.
    bairro = models.CharField(
        db_column='BAIRRO', max_length=40, blank=True, null=True)
    # Field name made lowercase.
    cidade = models.CharField(
        db_column='CIDADE', max_length=40, blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=8,
                           blank=True, null=True)
    # Field name made lowercase.
    cep_nota = models.IntegerField(db_column='CEP_NOTA', blank=True, null=True)
    # Field name made lowercase.
    match_end = models.CharField(
        db_column='MATCH_END', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    endereco = models.CharField(
        db_column='ENDERECO', max_length=130, blank=True, null=True)
    # Field name made lowercase.
    cadastro_id = models.IntegerField(db_column='CADASTRO_ID')
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(db_column='DT_INCLUSAO')
    # Field name made lowercase.
    dt_atualizacao = models.DateTimeField(
        db_column='DT_ATUALIZACAO', blank=True, null=True)
    # Field name made lowercase.
    dt_informacao = models.DateTimeField(
        db_column='DT_INFORMACAO', blank=True, null=True)
    # Field name made lowercase.
    match_geo = models.CharField(
        db_column='MATCH_GEO', max_length=32, blank=True, null=True)
    # Field name made lowercase.
    latitude = models.DecimalField(
        db_column='LATITUDE', max_digits=20, decimal_places=15, blank=True, null=True)
    # Field name made lowercase.
    longitude = models.DecimalField(
        db_column='LONGITUDE', max_digits=20, decimal_places=15, blank=True, null=True)
    # Field name made lowercase.
    status_geo = models.CharField(
        db_column='STATUS_GEO', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    cod_setor = models.CharField(
        db_column='COD_SETOR', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    origem_srs = models.CharField(
        db_column='ORIGEM_SRS', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    nsu = models.CharField(
        db_column='NSU', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    classificacao = models.CharField(
        db_column='CLASSIFICACAO', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    prioridade = models.IntegerField(
        db_column='PRIORIDADE', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HISTORICO_ENDERECOS_PJ'


class HistoricoEnderecoMailingListRank(models.Model):
    # Field name made lowercase.
    historico_enderecos_id = models.BigIntegerField(
        db_column='HISTORICO_ENDERECOS_ID')

    class Meta:
        managed = False
        db_table = 'HISTORICO_ENDERECO_MAILING_LIST_RANK'


class HistoricoMosaic(models.Model):
    # Field name made lowercase. The composite primary key (CONTATOS_ID, MOSAIC_ID, CD_MOSAIC) found, that is not supported. The first column is selected.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', primary_key=True)
    # Field name made lowercase.
    mosaic = models.ForeignKey(
        'MosaicVersao', models.DO_NOTHING, db_column='MOSAIC_ID')
    # Field name made lowercase.
    cd_mosaic = models.CharField(db_column='CD_MOSAIC', max_length=3)
    # Field name made lowercase.
    secondbest = models.CharField(
        db_column='SECONDBEST', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    distance = models.DecimalField(
        db_column='DISTANCE', max_digits=20, decimal_places=15, blank=True, null=True)
    # Field name made lowercase.
    affinity_score = models.DecimalField(
        db_column='AFFINITY_SCORE', max_digits=20, decimal_places=15, blank=True, null=True)
    # Field name made lowercase.
    affinity_percentile = models.CharField(
        db_column='AFFINITY_PERCENTILE', max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HISTORICO_MOSAIC'
        unique_together = (('contatos_id', 'mosaic', 'cd_mosaic'),)


class HistoricoTelefonesAssinantes(models.Model):
    historico_telefones_id = models.BigIntegerField(
        db_column='HISTORICO_TELEFONES_ID', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HISTORICO_TELEFONES_ASSINANTES'


class Iharticles(models.Model):
    article_id = models.AutoField(unique=True)
    name = models.CharField(max_length=128)
    publication_id = models.SmallIntegerField()
    table_id = models.IntegerField()
    publisher_id = models.SmallIntegerField()
    creation_script = models.CharField(max_length=255, blank=True, null=True)
    del_cmd = models.CharField(max_length=255, blank=True, null=True)
    filter = models.IntegerField()
    filter_clause = models.TextField(blank=True, null=True)
    ins_cmd = models.CharField(max_length=255, blank=True, null=True)
    pre_creation_cmd = models.SmallIntegerField()
    status = models.SmallIntegerField()
    type = models.SmallIntegerField()
    upd_cmd = models.CharField(max_length=255, blank=True, null=True)
    # This field type is a guess.
    schema_option = models.TextField(blank=True, null=True)
    dest_owner = models.CharField(max_length=128, blank=True, null=True)
    dest_table = models.CharField(max_length=128)
    tablespace_name = models.CharField(max_length=255, blank=True, null=True)
    objid = models.IntegerField(blank=True, null=True)
    sync_objid = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    publisher_status = models.IntegerField(blank=True, null=True)
    article_view_owner = models.CharField(
        max_length=255, blank=True, null=True)
    article_view = models.CharField(max_length=255, blank=True, null=True)
    ins_scripting_proc = models.IntegerField(blank=True, null=True)
    del_scripting_proc = models.IntegerField(blank=True, null=True)
    upd_scripting_proc = models.IntegerField(blank=True, null=True)
    custom_script = models.CharField(max_length=2048, blank=True, null=True)
    fire_triggers_on_snapshot = models.BooleanField()
    instance_id = models.IntegerField()
    use_default_datatypes = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'IHarticles'


class Ihcolumns(models.Model):
    column_id = models.AutoField()
    publishercolumn_id = models.IntegerField()
    name = models.CharField(max_length=128)
    article_id = models.IntegerField()
    column_ordinal = models.IntegerField()
    mapped_type = models.SmallIntegerField()
    mapped_length = models.BigIntegerField(blank=True, null=True)
    mapped_prec = models.IntegerField(blank=True, null=True)
    mapped_scale = models.IntegerField(blank=True, null=True)
    mapped_nullable = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IHcolumns'


class Ihconstrainttypes(models.Model):
    type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'IHconstrainttypes'


class Ihindextypes(models.Model):
    type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'IHindextypes'


class Ihpublications(models.Model):
    pubid = models.IntegerField()
    name = models.CharField(max_length=128)
    repl_freq = models.SmallIntegerField()
    status = models.SmallIntegerField()
    sync_method = models.SmallIntegerField()
    # This field type is a guess.
    snapshot_jobid = models.TextField(blank=True, null=True)
    enabled_for_internet = models.BooleanField()
    immediate_sync_ready = models.BooleanField()
    allow_queued_tran = models.BooleanField()
    allow_sync_tran = models.BooleanField()
    autogen_sync_procs = models.BooleanField()
    snapshot_in_defaultfolder = models.BooleanField()
    alt_snapshot_folder = models.CharField(
        max_length=510, blank=True, null=True)
    pre_snapshot_script = models.CharField(
        max_length=510, blank=True, null=True)
    post_snapshot_script = models.CharField(
        max_length=510, blank=True, null=True)
    compress_snapshot = models.BooleanField()
    ftp_address = models.CharField(max_length=128, blank=True, null=True)
    ftp_port = models.IntegerField()
    ftp_subdirectory = models.CharField(max_length=510, blank=True, null=True)
    ftp_login = models.CharField(max_length=256, blank=True, null=True)
    ftp_password = models.CharField(max_length=1048, blank=True, null=True)
    allow_dts = models.BooleanField()
    allow_anonymous = models.BooleanField()
    centralized_conflicts = models.BooleanField(blank=True, null=True)
    conflict_retention = models.IntegerField(blank=True, null=True)
    conflict_policy = models.IntegerField(blank=True, null=True)
    queue_type = models.IntegerField(blank=True, null=True)
    ad_guidname = models.CharField(max_length=128, blank=True, null=True)
    backward_comp_level = models.IntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    independent_agent = models.BooleanField()
    immediate_sync = models.BooleanField()
    allow_push = models.BooleanField()
    allow_pull = models.BooleanField()
    retention = models.IntegerField(blank=True, null=True)
    allow_subscription_copy = models.BooleanField()
    allow_initialize_from_backup = models.BooleanField()
    # This field type is a guess.
    min_autonosync_lsn = models.TextField(blank=True, null=True)
    replicate_ddl = models.IntegerField(blank=True, null=True)
    options = models.IntegerField(blank=True, null=True)
    originator_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IHpublications'


class Ihpublishercolumnconstraints(models.Model):
    publishercolumn_id = models.IntegerField()
    publisherconstraint_id = models.IntegerField()
    indid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'IHpublishercolumnconstraints'


class Ihpublishercolumnindexes(models.Model):
    publishercolumn_id = models.IntegerField()
    publisherindex_id = models.IntegerField()
    indid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'IHpublishercolumnindexes'


class Ihpublishercolumns(models.Model):
    publishercolumn_id = models.AutoField()
    table_id = models.IntegerField()
    publisher_id = models.SmallIntegerField()
    name = models.CharField(max_length=128)
    column_ordinal = models.IntegerField()
    type = models.CharField(max_length=255)
    length = models.BigIntegerField()
    prec = models.IntegerField(blank=True, null=True)
    scale = models.IntegerField(blank=True, null=True)
    isnullable = models.BooleanField()
    iscaptured = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'IHpublishercolumns'


class Ihpublisherconstraints(models.Model):
    publisherconstraint_id = models.AutoField(unique=True)
    table_id = models.IntegerField()
    publisher_id = models.SmallIntegerField()
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'IHpublisherconstraints'


class Ihpublisherindexes(models.Model):
    publisherindex_id = models.AutoField(unique=True)
    table_id = models.IntegerField()
    publisher_id = models.SmallIntegerField()
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'IHpublisherindexes'


class Ihpublishers(models.Model):
    publisher_id = models.SmallIntegerField()
    vendor = models.CharField(max_length=128)
    publisher_guid = models.CharField(max_length=36)
    flush_request_time = models.DateTimeField(blank=True, null=True)
    version = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IHpublishers'


class Ihpublishertables(models.Model):
    table_id = models.AutoField(unique=True)
    publisher_id = models.SmallIntegerField()
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'IHpublishertables'


class Ihsubscriptions(models.Model):
    article_id = models.IntegerField()
    srvid = models.SmallIntegerField()
    dest_db = models.CharField(max_length=128)
    login_name = models.CharField(max_length=128)
    distribution_jobid = models.TextField()  # This field type is a guess.
    # This field type is a guess.
    timestamp = models.TextField(blank=True, null=True)
    queued_reinit = models.BooleanField()
    status = models.SmallIntegerField()
    sync_type = models.SmallIntegerField()
    subscription_type = models.IntegerField()
    update_mode = models.SmallIntegerField()
    loopback_detection = models.BooleanField()
    nosync_type = models.SmallIntegerField()
    srvname = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'IHsubscriptions'
        unique_together = (('article_id', 'srvid', 'dest_db'),)


class ListaDdd(models.Model):
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    estado = models.CharField(
        db_column='ESTADO', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    cidade = models.CharField(
        db_column='CIDADE', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    codigo_ddd = models.SmallIntegerField(
        db_column='CODIGO_DDD', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LISTA_DDD'


class Mosaic(models.Model):
    # Field name made lowercase.
    cd_mosaic = models.CharField(db_column='CD_MOSAIC', max_length=3)
    # Field name made lowercase.
    cd_grupo = models.CharField(
        db_column='CD_GRUPO', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    cd_tipo = models.SmallIntegerField(db_column='CD_TIPO')
    # Field name made lowercase.
    ds_grupo = models.CharField(
        db_column='DS_GRUPO', max_length=40, blank=True, null=True)
    # Field name made lowercase.
    ds_tipo = models.CharField(
        db_column='DS_TIPO', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    descricao = models.TextField(db_column='DESCRICAO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MOSAIC'


class MosaicBusiness(models.Model):
    # Field name made lowercase.
    cd_mosaic_business = models.CharField(
        db_column='CD_MOSAIC_BUSINESS', max_length=3, blank=True, null=True)
    # Field name made lowercase.
    grupo_mosaic_business = models.CharField(
        db_column='GRUPO_MOSAIC_BUSINESS', max_length=28, blank=True, null=True)
    # Field name made lowercase.
    descr_mosaic_business = models.CharField(
        db_column='DESCR_MOSAIC_BUSINESS', max_length=43, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MOSAIC_BUSINESS'


class MosaicNovo(models.Model):
    # Field name made lowercase.
    novo_mosaic = models.CharField(
        db_column='Novo_Mosaic', max_length=4, blank=True, null=True)
    # Field name made lowercase.
    descricao = models.CharField(
        db_column='Descricao', max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MOSAIC_NOVO'


class MosaicVersao(models.Model):
    # Field name made lowercase.
    mosaic_id = models.AutoField(db_column='MOSAIC_ID', primary_key=True)
    # Field name made lowercase.
    mosaic_descr = models.CharField(
        db_column='MOSAIC_DESCR', unique=True, max_length=100)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(db_column='DT_INCLUSAO')

    class Meta:
        managed = False
        db_table = 'MOSAIC_VERSAO'


class MotivoSituacaoCadastral(models.Model):
    # Field name made lowercase.
    id_mts_cad = models.SmallAutoField(
        db_column='ID_MTS_CAD', primary_key=True, db_comment='- C¾digo Interno Sequencial do')
    # Field name made lowercase.
    desc_mts_cad = models.CharField(db_column='DESC_MTS_CAD', max_length=100,
                                    blank=True, null=True, db_comment='- Nome do Motivo da SituaþÒo C')
    # Field name made lowercase.
    cod_mts_cad = models.IntegerField(
        db_column='COD_MTS_CAD', blank=True, null=True, db_comment='- C¾digo do Motivo da SituaþÒo')

    class Meta:
        managed = False
        db_table = 'MOTIVO_SITUACAO_CADASTRAL'


class Msarticles(models.Model):
    publisher_id = models.SmallIntegerField()
    publisher_db = models.CharField(max_length=128, blank=True, null=True)
    publication_id = models.IntegerField()
    article = models.CharField(max_length=128)
    article_id = models.IntegerField()
    destination_object = models.CharField(
        max_length=128, blank=True, null=True)
    source_owner = models.CharField(max_length=128, blank=True, null=True)
    source_object = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    destination_owner = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSarticles'
        unique_together = (('publisher_id', 'publisher_db',
                           'publication_id', 'article', 'article_id'),)


class MscachedPeerLsns(models.Model):
    agent_id = models.IntegerField(blank=True, null=True)
    originator = models.CharField(max_length=128)
    originator_db = models.CharField(max_length=128)
    originator_publication_id = models.IntegerField(blank=True, null=True)
    originator_db_version = models.IntegerField(blank=True, null=True)
    originator_lsn = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MScached_peer_lsns'
        unique_together = (('agent_id', 'originator', 'originator_db',
                           'originator_publication_id', 'originator_db_version', 'originator_lsn'),)


class MsdistributionAgents(models.Model):
    id = models.AutoField(unique=True)
    name = models.CharField(max_length=100)
    publisher_database_id = models.IntegerField()
    publisher_id = models.SmallIntegerField()
    publisher_db = models.CharField(max_length=128)
    publication = models.CharField(max_length=128)
    subscriber_id = models.SmallIntegerField(blank=True, null=True)
    subscriber_db = models.CharField(max_length=128, blank=True, null=True)
    subscription_type = models.IntegerField()
    local_job = models.BooleanField(blank=True, null=True)
    # This field type is a guess.
    job_id = models.TextField(blank=True, null=True)
    subscription_guid = models.TextField()  # This field type is a guess.
    profile_id = models.IntegerField()
    anonymous_subid = models.CharField(max_length=36, blank=True, null=True)
    subscriber_name = models.CharField(max_length=128, blank=True, null=True)
    virtual_agent_id = models.IntegerField(blank=True, null=True)
    anonymous_agent_id = models.IntegerField(blank=True, null=True)
    creation_date = models.DateTimeField()
    queue_id = models.CharField(max_length=128, blank=True, null=True)
    queue_status = models.IntegerField()
    offload_enabled = models.BooleanField()
    offload_server = models.CharField(max_length=128, blank=True, null=True)
    dts_package_name = models.CharField(max_length=128, blank=True, null=True)
    dts_package_password = models.CharField(
        max_length=524, blank=True, null=True)
    dts_package_location = models.IntegerField()
    sid = models.BinaryField()
    queue_server = models.CharField(max_length=128, blank=True, null=True)
    subscriber_security_mode = models.SmallIntegerField(blank=True, null=True)
    subscriber_login = models.CharField(max_length=128, blank=True, null=True)
    subscriber_password = models.CharField(
        max_length=524, blank=True, null=True)
    reset_partial_snapshot_progress = models.BooleanField()
    job_step_uid = models.CharField(max_length=36, blank=True, null=True)
    subscriptionstreams = models.SmallIntegerField(blank=True, null=True)
    subscriber_type = models.SmallIntegerField(blank=True, null=True)
    subscriber_provider = models.CharField(
        max_length=128, blank=True, null=True)
    subscriber_datasrc = models.CharField(
        max_length=4000, blank=True, null=True)
    subscriber_location = models.CharField(
        max_length=4000, blank=True, null=True)
    subscriber_provider_string = models.CharField(
        max_length=4000, blank=True, null=True)
    subscriber_catalog = models.CharField(
        max_length=128, blank=True, null=True)
    memory_optimized = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSdistribution_agents'


class MsdistributionHistory(models.Model):
    agent_id = models.IntegerField()
    runstatus = models.IntegerField()
    start_time = models.DateTimeField()
    time = models.DateTimeField()
    duration = models.IntegerField()
    comments = models.TextField()
    xact_seqno = models.BinaryField(blank=True, null=True)
    current_delivery_rate = models.FloatField()
    current_delivery_latency = models.IntegerField()
    delivered_transactions = models.IntegerField()
    delivered_commands = models.IntegerField()
    average_commands = models.IntegerField()
    delivery_rate = models.FloatField()
    delivery_latency = models.IntegerField()
    total_delivered_commands = models.BigIntegerField()
    error_id = models.IntegerField()
    updateable_row = models.BooleanField()
    timestamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'MSdistribution_history'
        unique_together = (
            ('agent_id', 'runstatus', 'start_time', 'time', 'timestamp'),)


class MslogreaderAgents(models.Model):
    id = models.AutoField(unique=True)
    name = models.CharField(max_length=100)
    publisher_id = models.SmallIntegerField()
    publisher_db = models.CharField(max_length=128)
    publication = models.CharField(max_length=128)
    local_job = models.BooleanField()
    # This field type is a guess.
    job_id = models.TextField(blank=True, null=True)
    profile_id = models.IntegerField()
    publisher_security_mode = models.SmallIntegerField(blank=True, null=True)
    publisher_login = models.CharField(max_length=128, blank=True, null=True)
    publisher_password = models.CharField(
        max_length=524, blank=True, null=True)
    job_step_uid = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSlogreader_agents'


class MslogreaderHistory(models.Model):
    agent_id = models.IntegerField()
    runstatus = models.IntegerField()
    start_time = models.DateTimeField()
    time = models.DateTimeField()
    duration = models.IntegerField()
    comments = models.CharField(max_length=4000)
    xact_seqno = models.BinaryField(blank=True, null=True)
    delivery_time = models.IntegerField()
    delivered_transactions = models.IntegerField()
    delivered_commands = models.IntegerField()
    average_commands = models.IntegerField()
    delivery_rate = models.FloatField()
    delivery_latency = models.IntegerField()
    error_id = models.IntegerField()
    timestamp = models.TextField()  # This field type is a guess.
    updateable_row = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'MSlogreader_history'
        unique_together = (
            ('agent_id', 'runstatus', 'start_time', 'time', 'timestamp'),)


class MsmergeAgents(models.Model):
    id = models.AutoField(unique=True)
    name = models.CharField(max_length=100)
    publisher_id = models.SmallIntegerField()
    publisher_db = models.CharField(max_length=128)
    publication = models.CharField(max_length=128)
    subscriber_id = models.SmallIntegerField(blank=True, null=True)
    subscriber_db = models.CharField(max_length=128, blank=True, null=True)
    local_job = models.BooleanField(blank=True, null=True)
    # This field type is a guess.
    job_id = models.TextField(blank=True, null=True)
    profile_id = models.IntegerField(blank=True, null=True)
    anonymous_subid = models.CharField(max_length=36, blank=True, null=True)
    subscriber_name = models.CharField(max_length=128, blank=True, null=True)
    creation_date = models.DateTimeField()
    offload_enabled = models.BooleanField()
    offload_server = models.CharField(max_length=128, blank=True, null=True)
    sid = models.BinaryField()
    subscriber_security_mode = models.SmallIntegerField(blank=True, null=True)
    subscriber_login = models.CharField(max_length=128, blank=True, null=True)
    subscriber_password = models.CharField(
        max_length=524, blank=True, null=True)
    publisher_security_mode = models.SmallIntegerField(blank=True, null=True)
    publisher_login = models.CharField(max_length=128, blank=True, null=True)
    publisher_password = models.CharField(
        max_length=524, blank=True, null=True)
    job_step_uid = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSmerge_agents'


class MsmergeArticlehistory(models.Model):
    session_id = models.IntegerField()
    phase_id = models.IntegerField(blank=True, null=True)
    article_name = models.CharField(max_length=128, blank=True, null=True)
    start_time = models.DateTimeField()
    duration = models.IntegerField(blank=True, null=True)
    inserts = models.IntegerField()
    updates = models.IntegerField()
    deletes = models.IntegerField()
    conflicts = models.IntegerField()
    rows_retried = models.IntegerField()
    percent_complete = models.DecimalField(max_digits=5, decimal_places=2)
    estimated_changes = models.IntegerField(blank=True, null=True)
    relative_cost = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'MSmerge_articlehistory'
        unique_together = (('session_id', 'phase_id', 'article_name'),)


class MsmergeArticleresolver(models.Model):
    article_resolver = models.CharField(primary_key=True, max_length=255)
    resolver_clsid = models.CharField(max_length=50)
    is_dotnet_assembly = models.BooleanField(blank=True, null=True)
    dotnet_assembly_name = models.CharField(
        max_length=255, blank=True, null=True)
    dotnet_class_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSmerge_articleresolver'


class MsmergeHistory(models.Model):
    session_id = models.IntegerField(blank=True, null=True)
    agent_id = models.IntegerField()
    comments = models.CharField(max_length=1000)
    error_id = models.IntegerField()
    timestamp = models.TextField()  # This field type is a guess.
    updateable_row = models.BooleanField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'MSmerge_history'
        unique_together = (('agent_id', 'timestamp'),)


class MsmergeIdentityRangeAllocations(models.Model):
    publisher_id = models.SmallIntegerField()
    publisher_db = models.CharField(max_length=128)
    publication = models.CharField(max_length=128)
    article = models.CharField(max_length=128)
    subscriber = models.CharField(max_length=128, blank=True, null=True)
    subscriber_db = models.CharField(max_length=128, blank=True, null=True)
    is_pub_range = models.BooleanField()
    ranges_allocated = models.SmallIntegerField()
    range_begin = models.DecimalField(
        max_digits=38, decimal_places=0, blank=True, null=True)
    range_end = models.DecimalField(
        max_digits=38, decimal_places=0, blank=True, null=True)
    next_range_begin = models.DecimalField(
        max_digits=38, decimal_places=0, blank=True, null=True)
    next_range_end = models.DecimalField(
        max_digits=38, decimal_places=0, blank=True, null=True)
    max_used = models.DecimalField(max_digits=38, decimal_places=0)
    time_of_allocation = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSmerge_identity_range_allocations'


class MsmergeSessions(models.Model):
    session_id = models.AutoField(unique=True)
    agent_id = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    delivery_time = models.IntegerField()
    upload_time = models.IntegerField()
    download_time = models.IntegerField()
    schema_change_time = models.IntegerField()
    prepare_snapshot_time = models.IntegerField()
    delivery_rate = models.DecimalField(max_digits=12, decimal_places=2)
    time_remaining = models.IntegerField()
    percent_complete = models.DecimalField(max_digits=5, decimal_places=2)
    upload_inserts = models.IntegerField(blank=True, null=True)
    upload_updates = models.IntegerField(blank=True, null=True)
    upload_deletes = models.IntegerField(blank=True, null=True)
    upload_conflicts = models.IntegerField(blank=True, null=True)
    upload_rows_retried = models.IntegerField(blank=True, null=True)
    download_inserts = models.IntegerField(blank=True, null=True)
    download_updates = models.IntegerField(blank=True, null=True)
    download_deletes = models.IntegerField(blank=True, null=True)
    download_conflicts = models.IntegerField(blank=True, null=True)
    download_rows_retried = models.IntegerField(blank=True, null=True)
    schema_changes = models.IntegerField(blank=True, null=True)
    bulk_inserts = models.IntegerField(blank=True, null=True)
    metadata_rows_cleanedup = models.IntegerField(blank=True, null=True)
    runstatus = models.IntegerField()
    estimated_upload_changes = models.IntegerField(blank=True, null=True)
    estimated_download_changes = models.IntegerField(blank=True, null=True)
    connection_type = models.IntegerField(blank=True, null=True)
    timestamp = models.TextField()  # This field type is a guess.
    current_phase_id = models.IntegerField(blank=True, null=True)
    spid = models.SmallIntegerField(blank=True, null=True)
    spid_login_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSmerge_sessions'


class MsmergeSubscriptions(models.Model):
    publisher_id = models.SmallIntegerField()
    publisher_db = models.CharField(max_length=128, blank=True, null=True)
    publication_id = models.IntegerField()
    subscriber_id = models.SmallIntegerField(blank=True, null=True)
    subscriber_db = models.CharField(max_length=128, blank=True, null=True)
    subscription_type = models.IntegerField(blank=True, null=True)
    sync_type = models.SmallIntegerField()
    status = models.SmallIntegerField()
    subscription_time = models.DateTimeField()
    description = models.CharField(max_length=255, blank=True, null=True)
    publisher = models.CharField(max_length=128, blank=True, null=True)
    subscriber = models.CharField(max_length=128, blank=True, null=True)
    subid = models.CharField(unique=True, max_length=36)
    subscriber_version = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSmerge_subscriptions'
        unique_together = (('subscriber', 'subscriber_db',
                           'publisher_id', 'publisher_db', 'publication_id'),)


class Msnosyncsubsetup(models.Model):
    # The composite primary key (publisher_database_id, publication_id, artid, next_valid_lsn, parameterName) found, that is not supported. The first column is selected.
    publisher_database_id = models.IntegerField(primary_key=True)
    publication_id = models.IntegerField()
    artid = models.IntegerField()
    next_valid_lsn = models.BinaryField()
    # Field name made lowercase.
    parametername = models.CharField(db_column='parameterName', max_length=128)
    # Field name made lowercase.
    parametervalue = models.TextField(
        db_column='parameterValue', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSnosyncsubsetup'
        unique_together = (('publisher_database_id', 'publication_id',
                           'artid', 'next_valid_lsn', 'parametername'),)


class MspublicationAccess(models.Model):
    publication_id = models.IntegerField(blank=True, null=True)
    login = models.CharField(max_length=128)
    sid = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSpublication_access'
        unique_together = (('publication_id', 'sid'),)


class Mspublications(models.Model):
    publisher_id = models.SmallIntegerField()
    publisher_db = models.CharField(max_length=128, blank=True, null=True)
    publication = models.CharField(max_length=128)
    publication_id = models.AutoField()
    publication_type = models.IntegerField()
    thirdparty_flag = models.BooleanField()
    independent_agent = models.BooleanField()
    immediate_sync = models.BooleanField()
    allow_push = models.BooleanField()
    allow_pull = models.BooleanField()
    allow_anonymous = models.BooleanField()
    description = models.CharField(max_length=255, blank=True, null=True)
    vendor_name = models.CharField(max_length=100, blank=True, null=True)
    retention = models.IntegerField(blank=True, null=True)
    sync_method = models.IntegerField()
    allow_subscription_copy = models.BooleanField()
    thirdparty_options = models.IntegerField(blank=True, null=True)
    allow_queued_tran = models.BooleanField()
    options = models.IntegerField()
    retention_period_unit = models.SmallIntegerField()
    allow_initialize_from_backup = models.BooleanField()
    min_autonosync_lsn = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSpublications'
        unique_together = (('publisher_id', 'publisher_db', 'publication',
                           'publication_id'), ('publication', 'publisher_db', 'publisher_id'),)


class Mspublicationthresholds(models.Model):
    publication_id = models.IntegerField()
    metric_id = models.IntegerField()
    # This field type is a guess.
    value = models.TextField(blank=True, null=True)
    shouldalert = models.BooleanField()
    isenabled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'MSpublicationthresholds'
        unique_together = (('publication_id', 'metric_id'),)


class MspublisherDatabases(models.Model):
    publisher_id = models.SmallIntegerField()
    publisher_db = models.CharField(max_length=128, blank=True, null=True)
    id = models.AutoField()
    publisher_engine_edition = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSpublisher_databases'
        unique_together = (('publisher_id', 'publisher_db', 'id'),)


class MsqreaderAgents(models.Model):
    id = models.AutoField(unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    # This field type is a guess.
    job_id = models.TextField(blank=True, null=True)
    profile_id = models.IntegerField(blank=True, null=True)
    job_step_uid = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSqreader_agents'


class MsqreaderHistory(models.Model):
    agent_id = models.IntegerField()
    publication_id = models.IntegerField(blank=True, null=True)
    runstatus = models.IntegerField()
    start_time = models.DateTimeField()
    time = models.DateTimeField()
    duration = models.IntegerField()
    comments = models.CharField(max_length=1000)
    transaction_id = models.CharField(max_length=40, blank=True, null=True)
    transaction_status = models.IntegerField(blank=True, null=True)
    transactions_processed = models.IntegerField(blank=True, null=True)
    commands_processed = models.IntegerField(blank=True, null=True)
    delivery_rate = models.FloatField()
    transaction_rate = models.FloatField()
    subscriber = models.CharField(max_length=128, blank=True, null=True)
    subscriberdb = models.CharField(max_length=128, blank=True, null=True)
    error_id = models.IntegerField(blank=True, null=True)
    timestamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'MSqreader_history'


class MsredirectedPublishers(models.Model):
    original_publisher = models.CharField(max_length=128)
    publisher_db = models.CharField(max_length=128)
    redirected_publisher = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'MSredirected_publishers'
        unique_together = (('original_publisher', 'publisher_db'),)


class MsreplBackupLsns(models.Model):
    publisher_database_id = models.IntegerField(unique=True)
    valid_xact_id = models.BinaryField(blank=True, null=True)
    valid_xact_seqno = models.BinaryField(blank=True, null=True)
    next_xact_id = models.BinaryField(blank=True, null=True)
    next_xact_seqno = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSrepl_backup_lsns'


class MsreplCommands(models.Model):
    publisher_database_id = models.IntegerField()
    xact_seqno = models.BinaryField()
    type = models.IntegerField()
    article_id = models.IntegerField()
    originator_id = models.IntegerField()
    command_id = models.IntegerField()
    partial_command = models.BooleanField()
    command = models.BinaryField(blank=True, null=True)
    hashkey = models.IntegerField(blank=True, null=True)
    originator_lsn = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSrepl_commands'
        unique_together = (
            ('publisher_database_id', 'xact_seqno', 'command_id'),)


class MsreplErrors(models.Model):
    id = models.IntegerField()
    time = models.DateTimeField()
    error_type_id = models.IntegerField(blank=True, null=True)
    source_type_id = models.IntegerField(blank=True, null=True)
    source_name = models.CharField(max_length=100, blank=True, null=True)
    error_code = models.CharField(max_length=128, blank=True, null=True)
    error_text = models.TextField(blank=True, null=True)
    xact_seqno = models.BinaryField(blank=True, null=True)
    command_id = models.IntegerField(blank=True, null=True)
    session_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSrepl_errors'


class MsreplIdentityRange(models.Model):
    # The composite primary key (publisher, publisher_db, tablename) found, that is not supported. The first column is selected.
    publisher = models.CharField(primary_key=True, max_length=128)
    publisher_db = models.CharField(max_length=128)
    tablename = models.CharField(max_length=128)
    identity_support = models.IntegerField(blank=True, null=True)
    next_seed = models.BigIntegerField(blank=True, null=True)
    pub_range = models.BigIntegerField(blank=True, null=True)
    range = models.BigIntegerField(blank=True, null=True)
    max_identity = models.BigIntegerField(blank=True, null=True)
    threshold = models.IntegerField(blank=True, null=True)
    current_max = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSrepl_identity_range'
        unique_together = (('publisher', 'publisher_db', 'tablename'),)


class MsreplOriginators(models.Model):
    id = models.AutoField()
    publisher_database_id = models.IntegerField()
    srvname = models.CharField(max_length=128)
    dbname = models.CharField(max_length=128)
    publication_id = models.IntegerField(blank=True, null=True)
    dbversion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSrepl_originators'
        unique_together = (
            ('id', 'srvname', 'dbname', 'publication_id', 'dbversion'),)


class MsreplTransactions(models.Model):
    publisher_database_id = models.IntegerField()
    xact_id = models.BinaryField(blank=True, null=True)
    xact_seqno = models.BinaryField()
    entry_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'MSrepl_transactions'
        unique_together = (('publisher_database_id', 'xact_seqno'),)


class MsreplVersion(models.Model):
    major_version = models.IntegerField()
    minor_version = models.IntegerField()
    revision = models.IntegerField()
    db_existed = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSrepl_version'
        unique_together = (('major_version', 'minor_version', 'revision'),)


class MsreplicationMonitordata(models.Model):
    lastrefresh = models.DateTimeField(blank=True, null=True)
    computetime = models.IntegerField(blank=True, null=True)
    publication_id = models.IntegerField(blank=True, null=True)
    publisher = models.CharField(max_length=128)
    publisher_srvid = models.IntegerField(blank=True, null=True)
    publisher_db = models.CharField(max_length=128)
    publication = models.CharField(max_length=128)
    publication_type = models.IntegerField(blank=True, null=True)
    agent_type = models.IntegerField(blank=True, null=True)
    agent_id = models.IntegerField(blank=True, null=True)
    agent_name = models.CharField(max_length=128)
    job_id = models.CharField(max_length=36, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    isagentrunningnow = models.BooleanField(blank=True, null=True)
    warning = models.IntegerField(blank=True, null=True)
    last_distsync = models.DateTimeField(blank=True, null=True)
    agentstoptime = models.DateTimeField(blank=True, null=True)
    distdb = models.CharField(max_length=128, blank=True, null=True)
    retention = models.IntegerField(blank=True, null=True)
    time_stamp = models.DateTimeField(blank=True, null=True)
    worst_latency = models.IntegerField(blank=True, null=True)
    best_latency = models.IntegerField(blank=True, null=True)
    avg_latency = models.IntegerField(blank=True, null=True)
    cur_latency = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    worst_runspeedperf = models.IntegerField(
        db_column='worst_runspeedPerf', blank=True, null=True)
    # Field name made lowercase.
    best_runspeedperf = models.IntegerField(
        db_column='best_runspeedPerf', blank=True, null=True)
    # Field name made lowercase.
    average_runspeedperf = models.IntegerField(
        db_column='average_runspeedPerf', blank=True, null=True)
    # Field name made lowercase.
    mergeperformance = models.IntegerField(
        db_column='mergePerformance', blank=True, null=True)
    mergelatestsessionrunduration = models.IntegerField(blank=True, null=True)
    mergelatestsessionrunspeed = models.FloatField(blank=True, null=True)
    mergelatestsessionconnectiontype = models.IntegerField(
        blank=True, null=True)
    retention_period_unit = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSreplication_monitordata'


class MssnapshotAgents(models.Model):
    id = models.AutoField(unique=True)
    name = models.CharField(max_length=100)
    publisher_id = models.SmallIntegerField()
    publisher_db = models.CharField(max_length=128)
    publication = models.CharField(max_length=128)
    publication_type = models.IntegerField()
    local_job = models.BooleanField()
    # This field type is a guess.
    job_id = models.TextField(blank=True, null=True)
    profile_id = models.IntegerField()
    dynamic_filter_login = models.CharField(
        max_length=128, blank=True, null=True)
    dynamic_filter_hostname = models.CharField(
        max_length=128, blank=True, null=True)
    publisher_security_mode = models.IntegerField(blank=True, null=True)
    publisher_login = models.CharField(max_length=128, blank=True, null=True)
    publisher_password = models.CharField(
        max_length=524, blank=True, null=True)
    job_step_uid = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSsnapshot_agents'


class MssnapshotHistory(models.Model):
    agent_id = models.IntegerField()
    runstatus = models.IntegerField()
    start_time = models.DateTimeField()
    time = models.DateTimeField()
    duration = models.IntegerField()
    comments = models.CharField(max_length=1000)
    delivered_transactions = models.IntegerField()
    delivered_commands = models.IntegerField()
    delivery_rate = models.FloatField()
    error_id = models.IntegerField()
    timestamp = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'MSsnapshot_history'
        unique_together = (('agent_id', 'start_time', 'time', 'timestamp'),)


class MssubscriberInfo(models.Model):
    publisher = models.CharField(max_length=128)
    subscriber = models.CharField(max_length=128)
    type = models.SmallIntegerField()
    login = models.CharField(max_length=128, blank=True, null=True)
    password = models.CharField(max_length=524, blank=True, null=True)
    description = models.CharField(max_length=510, blank=True, null=True)
    security_mode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'MSsubscriber_info'
        unique_together = (('publisher', 'subscriber'),)


class MssubscriberSchedule(models.Model):
    publisher = models.CharField(max_length=128)
    subscriber = models.CharField(max_length=128)
    agent_type = models.SmallIntegerField()
    frequency_type = models.IntegerField()
    frequency_interval = models.IntegerField()
    frequency_relative_interval = models.IntegerField()
    frequency_recurrence_factor = models.IntegerField()
    frequency_subday = models.IntegerField()
    frequency_subday_interval = models.IntegerField()
    active_start_time_of_day = models.IntegerField()
    active_end_time_of_day = models.IntegerField()
    active_start_date = models.IntegerField()
    active_end_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'MSsubscriber_schedule'
        unique_together = (('publisher', 'subscriber', 'agent_type'),)


class Mssubscriptions(models.Model):
    publisher_database_id = models.IntegerField()
    publisher_id = models.SmallIntegerField()
    publisher_db = models.CharField(max_length=128)
    publication_id = models.IntegerField()
    article_id = models.IntegerField()
    subscriber_id = models.SmallIntegerField()
    subscriber_db = models.CharField(max_length=128)
    subscription_type = models.IntegerField()
    sync_type = models.SmallIntegerField()
    status = models.SmallIntegerField()
    subscription_seqno = models.BinaryField()
    snapshot_seqno_flag = models.BooleanField()
    independent_agent = models.BooleanField()
    subscription_time = models.DateTimeField()
    loopback_detection = models.BooleanField()
    agent_id = models.IntegerField()
    update_mode = models.SmallIntegerField()
    publisher_seqno = models.BinaryField()
    ss_cplt_seqno = models.BinaryField()
    nosync_type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'MSsubscriptions'
        unique_together = (('article_id', 'agent_id'),)


class MssyncStates(models.Model):
    publisher_id = models.SmallIntegerField()
    publisher_db = models.CharField(max_length=128)
    publication_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'MSsync_states'
        unique_together = (('publisher_id', 'publisher_db', 'publication_id'),)


class MstracerHistory(models.Model):
    # The composite primary key (parent_tracer_id, agent_id) found, that is not supported. The first column is selected.
    parent_tracer = models.OneToOneField(
        'MstracerTokens', models.DO_NOTHING, primary_key=True)
    agent_id = models.IntegerField()
    subscriber_commit = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MStracer_history'
        unique_together = (('parent_tracer', 'agent_id'),)


class MstracerTokens(models.Model):
    tracer_id = models.AutoField(primary_key=True)
    publication_id = models.IntegerField()
    publisher_commit = models.DateTimeField()
    distributor_commit = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MStracer_tokens'


class Mt(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    nasc = models.CharField(max_length=100, blank=True, null=True)
    cpf = models.CharField(max_length=100, blank=True, null=True)
    salario = models.CharField(max_length=100, blank=True, null=True)
    sexo = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    uf = models.CharField(max_length=100, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MT'


class Nacionalidade(models.Model):
    # Field name made lowercase.
    id_nac = models.IntegerField(db_column='ID_NAC', primary_key=True)
    # Field name made lowercase.
    desc_nac = models.CharField(db_column='DESC_NAC', max_length=100)

    class Meta:
        managed = False
        db_table = 'NACIONALIDADE'


class Naturalidade(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    naturalidade_cidade = models.CharField(
        db_column='NATURALIDADE_CIDADE', max_length=72)
    # Field name made lowercase.
    naturalidade_uf = models.CharField(
        db_column='NATURALIDADE_UF', max_length=2)
    # Field name made lowercase.
    dt_informacao = models.DateTimeField(
        db_column='DT_INFORMACAO', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id_naturalidade = models.IntegerField(
        db_column='CADASTRO_ID_NATURALIDADE')

    class Meta:
        managed = False
        db_table = 'NATURALIDADE'


class OcorrenciaIndices(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    # Field name made lowercase.
    servidor = models.CharField(db_column='SERVIDOR', max_length=100)
    # Field name made lowercase.
    tabela = models.CharField(db_column='TABELA', max_length=100)
    # Field name made lowercase.
    indice = models.CharField(db_column='INDICE', max_length=255)
    # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=100)

    class Meta:
        managed = False
        db_table = 'OCORRENCIA_INDICES'


class Ocupacao(models.Model):
    cbo = models.IntegerField(db_column='CBO',)  # Field name made lowercase.
    titulo = models.CharField(max_length=255)
    # Field name made lowercase.
    codfamilia = models.SmallIntegerField(db_column='CodFamilia')
    # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=8)

    class Meta:
        managed = False
        db_table = 'OCUPACAO'


class OrigemNosolicitor(models.Model):
    # Field name made lowercase.
    cd_ori = models.SmallIntegerField(
        db_column='CD_ORI', primary_key=True, db_comment='- C¾digo Interno Sequencial da')
    # Field name made lowercase.
    ds_ori = models.CharField(db_column='DS_ORI', max_length=100,
                              blank=True, null=True, db_comment='- Nome da Origem do Bloqueio d')
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True, db_comment='- Data d aInclusÒo da Origem d')

    class Meta:
        managed = False
        db_table = 'ORIGEM_NOSOLICITOR'


class Pa(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    nasc = models.CharField(max_length=100, blank=True, null=True)
    cpf = models.CharField(max_length=100, blank=True, null=True)
    salario = models.CharField(max_length=100, blank=True, null=True)
    sexo = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    uf = models.CharField(max_length=100, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PA'


class PessoaFisica(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    cpf = models.CharField(
        db_column='CPF', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    nome = models.CharField(
        db_column='NOME', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    nome_primeiro = models.CharField(
        db_column='NOME_PRIMEIRO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    nome_meio = models.CharField(
        db_column='NOME_MEIO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    nome_ultimo = models.CharField(
        db_column='NOME_ULTIMO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    match_nome = models.CharField(
        db_column='MATCH_NOME', max_length=35, blank=True, null=True)
    # Field name made lowercase.
    match_nome_todas_particulas = models.CharField(
        db_column='MATCH_NOME_TODAS_PARTICULAS', max_length=62, blank=True, null=True)
    # Field name made lowercase.
    nome_nota = models.CharField(
        db_column='NOME_NOTA', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    sexo = models.CharField(
        db_column='SEXO', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    nasc = models.DateTimeField(db_column='NASC', blank=True, null=True)
    # Field name made lowercase.
    nome_civil = models.CharField(
        db_column='NOME_CIVIL', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    nome_mae = models.CharField(
        db_column='NOME_MAE', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    nome_pai = models.CharField(
        db_column='NOME_PAI', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    match_nome_mae = models.CharField(
        db_column='MATCH_NOME_MAE', max_length=35, blank=True, null=True)
    # Field name made lowercase.
    match_nome_pai = models.CharField(
        db_column='MATCH_NOME_PAI', max_length=35, blank=True, null=True)
    # Field name made lowercase.
    cadastro_id = models.IntegerField(
        db_column='CADASTRO_ID', blank=True, null=True)
    # Field name made lowercase.
    estciv = models.CharField(
        db_column='ESTCIV', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    cadastro_id_estciv = models.IntegerField(
        db_column='CADASTRO_ID_ESTCIV', blank=True, null=True)
    # Field name made lowercase.
    rg = models.CharField(db_column='RG', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    cadastro_id_rg = models.IntegerField(
        db_column='CADASTRO_ID_RG', blank=True, null=True)
    # Field name made lowercase.
    nacionalid = models.IntegerField(
        db_column='NACIONALID', blank=True, null=True)
    cadastro_id_nacionalidade = models.IntegerField(
        db_column='CADASTRO_ID_NACIONALIDADE', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    contatos_id_conjuge = models.BigIntegerField(
        db_column='CONTATOS_ID_CONJUGE', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id_conjuge = models.IntegerField(
        db_column='CADASTRO_ID_CONJUGE', blank=True, null=True)
    # Field name made lowercase.
    so = models.BooleanField(db_column='SO', blank=True, null=True)
    # Field name made lowercase.
    cd_sit_cad = models.SmallIntegerField(
        db_column='CD_SIT_CAD', blank=True, null=True)
    # Field name made lowercase.
    dt_sit_cad = models.DateTimeField(
        db_column='DT_SIT_CAD', blank=True, null=True)
    # Field name made lowercase.
    dt_informacao = models.DateTimeField(
        db_column='DT_INFORMACAO', blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)
    # Field name made lowercase.
    dt_atualizacao = models.DateTimeField(
        db_column='DT_ATUALIZACAO', blank=True, null=True)
    # Field name made lowercase.
    nota = models.CharField(
        db_column='NOTA', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    cpf_conj = models.CharField(
        db_column='CPF_CONJ', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    sexo_retratado = models.CharField(
        db_column='SEXO_RETRATADO', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    cadastro_id_so = models.IntegerField(
        db_column='CADASTRO_ID_SO', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id_sitcad = models.IntegerField(
        db_column='CADASTRO_ID_SITCAD', blank=True, null=True)
    # Field name made lowercase.
    ob_unb = models.BooleanField(db_column='OB_UNB', blank=True, null=True)
    # Field name made lowercase.
    unb_estciv = models.CharField(
        db_column='UNB_ESTCIV', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    unb_rg = models.CharField(
        db_column='UNB_RG', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    unb_cpf_conjuge = models.CharField(
        db_column='UNB_CPF_CONJUGE', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    inibir = models.SmallIntegerField(
        db_column='INIBIR', blank=True, null=True)
    # Field name made lowercase.
    cbo = models.IntegerField(db_column='CBO', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id_cbo = models.IntegerField(
        db_column='CADASTRO_ID_CBO', blank=True, null=True)
    # Field name made lowercase.
    orgao_emissor = models.CharField(
        db_column='ORGAO_EMISSOR', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    uf_emissao = models.CharField(
        db_column='UF_EMISSAO', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    cod_controle = models.CharField(
        db_column='COD_CONTROLE', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    hr_sit_cad = models.CharField(
        db_column='HR_SIT_CAD', max_length=8, blank=True, null=True)
    # Field name made lowercase.
    dt_ob = models.DateTimeField(db_column='DT_OB', blank=True, null=True)
    # Field name made lowercase.
    cd_mosaic = models.CharField(
        db_column='CD_MOSAIC', max_length=3, blank=True, null=True)
    # Field name made lowercase.
    secondbest = models.CharField(
        db_column='SECONDBEST', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    distance = models.DecimalField(
        db_column='DISTANCE', max_digits=20, decimal_places=15, blank=True, null=True)
    # Field name made lowercase.
    affinity_score = models.DecimalField(
        db_column='AFFINITY_SCORE', max_digits=20, decimal_places=15, blank=True, null=True)
    # Field name made lowercase.
    affinity_percentile = models.CharField(
        db_column='AFFINITY_PERCENTILE', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    email = models.CharField(
        db_column='EMAIL', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    household_id = models.BigIntegerField(
        db_column='HOUSEHOLD_ID', blank=True, null=True)
    # Field name made lowercase.
    household_id_2016 = models.IntegerField(
        db_column='HOUSEHOLD_ID_2016', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id_nasc = models.IntegerField(
        db_column='CADASTRO_ID_NASC', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id_nome_mae = models.IntegerField(
        db_column='CADASTRO_ID_NOME_MAE', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id_nome_pai = models.IntegerField(
        db_column='CADASTRO_ID_NOME_PAI', blank=True, null=True)
    # Field name made lowercase.
    renda = models.DecimalField(
        db_column='RENDA', max_digits=8, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    faixa_renda_id = models.IntegerField(
        db_column='FAIXA_RENDA_ID', blank=True, null=True)
    # Field name made lowercase.
    flag_serv_pb = models.BooleanField(
        db_column='FLAG_SERV_PB', blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao_serv_pb = models.DateTimeField(
        db_column='DT_INCLUSAO_SERV_PB', blank=True, null=True)
    # Field name made lowercase.
    dt_atualizacao_serv_pb = models.DateTimeField(
        db_column='DT_ATUALIZACAO_SERV_PB', blank=True, null=True)
    # Field name made lowercase.
    titulo_eleitor = models.CharField(
        db_column='TITULO_ELEITOR', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    cd_mosaic_novo = models.CharField(
        db_column='CD_MOSAIC_NOVO', max_length=3, blank=True, null=True)
    # Field name made lowercase.
    cd_mosaic_secundario = models.CharField(
        db_column='CD_MOSAIC_SECUNDARIO', max_length=3, blank=True, null=True)
    # Field name made lowercase.
    mosaic_segment_alternative = models.CharField(
        db_column='MOSAIC_SEGMENT_ALTERNATIVE', max_length=5, blank=True, null=True)
    # Field name made lowercase.
    mosaic_segment = models.CharField(
        db_column='MOSAIC_SEGMENT', max_length=3, blank=True, null=True)
    # Field name made lowercase.
    mosaic_global = models.CharField(
        db_column='MOSAIC_GLOBAL', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    mosaicfactor1 = models.CharField(
        db_column='MOSAICFACTOR1', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    mosaicfactor2 = models.CharField(
        db_column='MOSAICFACTOR2', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    mosaicfactor3 = models.CharField(
        db_column='MOSAICFACTOR3', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    mosaicfactor4 = models.CharField(
        db_column='MOSAICFACTOR4', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    mosaicfactor5 = models.CharField(
        db_column='MOSAICFACTOR5', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    mosaic_origem = models.CharField(
        db_column='MOSAIC_ORIGEM', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    mother_score = models.CharField(
        db_column='MOTHER_SCORE', max_length=2, blank=True, null=True)
    nr_cpf = models.BigIntegerField(blank=True, null=True)
    # Field name made lowercase.
    origem_dado_topdados = models.CharField(
        db_column='ORIGEM_DADO_TOPDADOS', max_length=100)
    # Field name made lowercase.
    id_usuario_consultou = models.IntegerField(
        db_column='ID_USUARIO_CONSULTOU', blank=True, null=True)
    # Field name made lowercase.
    dt_sci_data_consulta = models.DateTimeField(
        db_column='DT_SCI_DATA_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    rg_data_emissao = models.CharField(
        db_column='RG_DATA_EMISSAO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    cnh = models.CharField(
        db_column='CNH', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    data_habilitacao = models.CharField(
        db_column='DATA_HABILITACAO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    cod_seguranca = models.CharField(
        db_column='COD_SEGURANCA', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    formulario_cnh = models.CharField(
        db_column='FORMULARIO_CNH', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    formulario_renach = models.CharField(
        db_column='FORMULARIO_RENACH', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    numero_pgu = models.CharField(
        db_column='NUMERO_PGU', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    categorial_atual = models.CharField(
        db_column='CATEGORIAL_ATUAL', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    situacao_cnh = models.CharField(
        db_column='SITUACAO_CNH', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    dt_ultima_emissao = models.CharField(
        db_column='DT_ULTIMA_EMISSAO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    data_validade = models.CharField(
        db_column='DATA_VALIDADE', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    local_emissao = models.CharField(
        db_column='LOCAL_EMISSAO', max_length=30, blank=True, null=True)
    dt_bigdata_data_consulta = models.DateTimeField(
        db_column='DT_BIGDATA_DATA_CONSULTA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PESSOA_FISICA'


class PessoaFisicaHistoricoAlteracao(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    cpf = models.CharField(
        db_column='CPF', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    nome = models.CharField(
        db_column='NOME', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    nome_primeiro = models.CharField(
        db_column='NOME_PRIMEIRO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    nome_meio = models.CharField(
        db_column='NOME_MEIO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    nome_ultimo = models.CharField(
        db_column='NOME_ULTIMO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    match_nome = models.CharField(
        db_column='MATCH_NOME', max_length=35, blank=True, null=True)
    # Field name made lowercase.
    match_nome_todas_particulas = models.CharField(
        db_column='MATCH_NOME_TODAS_PARTICULAS', max_length=62, blank=True, null=True)
    # Field name made lowercase.
    nome_nota = models.CharField(
        db_column='NOME_NOTA', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    sexo = models.CharField(
        db_column='SEXO', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    nasc = models.DateTimeField(db_column='NASC', blank=True, null=True)
    # Field name made lowercase.
    nome_civil = models.CharField(
        db_column='NOME_CIVIL', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    nome_mae = models.CharField(
        db_column='NOME_MAE', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    nome_pai = models.CharField(
        db_column='NOME_PAI', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    match_nome_mae = models.CharField(
        db_column='MATCH_NOME_MAE', max_length=35, blank=True, null=True)
    # Field name made lowercase.
    match_nome_pai = models.CharField(
        db_column='MATCH_NOME_PAI', max_length=35, blank=True, null=True)
    # Field name made lowercase.
    cadastro_id = models.IntegerField(
        db_column='CADASTRO_ID', blank=True, null=True)
    # Field name made lowercase.
    estciv = models.CharField(
        db_column='ESTCIV', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    cadastro_id_estciv = models.IntegerField(
        db_column='CADASTRO_ID_ESTCIV', blank=True, null=True)
    # Field name made lowercase.
    rg = models.CharField(db_column='RG', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    cadastro_id_rg = models.IntegerField(
        db_column='CADASTRO_ID_RG', blank=True, null=True)
    # Field name made lowercase.
    nacionalid = models.IntegerField(
        db_column='NACIONALID', blank=True, null=True)
    cadastro_id_nacionalidade = models.IntegerField(
        db_column='CADASTRO_ID_NACIONALIDADE', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    contatos_id_conjuge = models.BigIntegerField(
        db_column='CONTATOS_ID_CONJUGE', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id_conjuge = models.IntegerField(
        db_column='CADASTRO_ID_CONJUGE', blank=True, null=True)
    # Field name made lowercase.
    so = models.BooleanField(db_column='SO', blank=True, null=True)
    # Field name made lowercase.
    cd_sit_cad = models.SmallIntegerField(
        db_column='CD_SIT_CAD', blank=True, null=True)
    # Field name made lowercase.
    dt_sit_cad = models.DateTimeField(
        db_column='DT_SIT_CAD', blank=True, null=True)
    # Field name made lowercase.
    dt_informacao = models.DateTimeField(
        db_column='DT_INFORMACAO', blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)
    # Field name made lowercase.
    dt_atualizacao = models.DateTimeField(
        db_column='DT_ATUALIZACAO', blank=True, null=True)
    # Field name made lowercase.
    nota = models.CharField(
        db_column='NOTA', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    cpf_conj = models.CharField(
        db_column='CPF_CONJ', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    sexo_retratado = models.CharField(
        db_column='SEXO_RETRATADO', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    cadastro_id_so = models.IntegerField(
        db_column='CADASTRO_ID_SO', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id_sitcad = models.IntegerField(
        db_column='CADASTRO_ID_SITCAD', blank=True, null=True)
    # Field name made lowercase.
    ob_unb = models.BooleanField(db_column='OB_UNB', blank=True, null=True)
    # Field name made lowercase.
    unb_estciv = models.CharField(
        db_column='UNB_ESTCIV', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    unb_rg = models.CharField(
        db_column='UNB_RG', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    unb_cpf_conjuge = models.CharField(
        db_column='UNB_CPF_CONJUGE', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    inibir = models.SmallIntegerField(
        db_column='INIBIR', blank=True, null=True)
    # Field name made lowercase.
    cbo = models.IntegerField(db_column='CBO', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id_cbo = models.IntegerField(
        db_column='CADASTRO_ID_CBO', blank=True, null=True)
    # Field name made lowercase.
    orgao_emissor = models.CharField(
        db_column='ORGAO_EMISSOR', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    uf_emissao = models.CharField(
        db_column='UF_EMISSAO', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    cod_controle = models.CharField(
        db_column='COD_CONTROLE', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    hr_sit_cad = models.CharField(
        db_column='HR_SIT_CAD', max_length=8, blank=True, null=True)
    # Field name made lowercase.
    dt_ob = models.DateTimeField(db_column='DT_OB', blank=True, null=True)
    # Field name made lowercase.
    cd_mosaic = models.CharField(
        db_column='CD_MOSAIC', max_length=3, blank=True, null=True)
    # Field name made lowercase.
    secondbest = models.CharField(
        db_column='SECONDBEST', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    distance = models.DecimalField(
        db_column='DISTANCE', max_digits=20, decimal_places=15, blank=True, null=True)
    # Field name made lowercase.
    affinity_score = models.DecimalField(
        db_column='AFFINITY_SCORE', max_digits=20, decimal_places=15, blank=True, null=True)
    # Field name made lowercase.
    affinity_percentile = models.CharField(
        db_column='AFFINITY_PERCENTILE', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    email = models.CharField(
        db_column='EMAIL', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    household_id = models.BigIntegerField(
        db_column='HOUSEHOLD_ID', blank=True, null=True)
    # Field name made lowercase.
    household_id_2016 = models.IntegerField(
        db_column='HOUSEHOLD_ID_2016', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id_nasc = models.IntegerField(
        db_column='CADASTRO_ID_NASC', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id_nome_mae = models.IntegerField(
        db_column='CADASTRO_ID_NOME_MAE', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id_nome_pai = models.IntegerField(
        db_column='CADASTRO_ID_NOME_PAI', blank=True, null=True)
    # Field name made lowercase.
    renda = models.DecimalField(
        db_column='RENDA', max_digits=8, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    faixa_renda_id = models.IntegerField(
        db_column='FAIXA_RENDA_ID', blank=True, null=True)
    # Field name made lowercase.
    flag_serv_pb = models.BooleanField(
        db_column='FLAG_SERV_PB', blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao_serv_pb = models.DateTimeField(
        db_column='DT_INCLUSAO_SERV_PB', blank=True, null=True)
    # Field name made lowercase.
    dt_atualizacao_serv_pb = models.DateTimeField(
        db_column='DT_ATUALIZACAO_SERV_PB', blank=True, null=True)
    # Field name made lowercase.
    titulo_eleitor = models.CharField(
        db_column='TITULO_ELEITOR', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    cd_mosaic_novo = models.CharField(
        db_column='CD_MOSAIC_NOVO', max_length=3, blank=True, null=True)
    # Field name made lowercase.
    cd_mosaic_secundario = models.CharField(
        db_column='CD_MOSAIC_SECUNDARIO', max_length=3, blank=True, null=True)
    # Field name made lowercase.
    mosaic_segment_alternative = models.CharField(
        db_column='MOSAIC_SEGMENT_ALTERNATIVE', max_length=5, blank=True, null=True)
    # Field name made lowercase.
    mosaic_segment = models.CharField(
        db_column='MOSAIC_SEGMENT', max_length=3, blank=True, null=True)
    # Field name made lowercase.
    mosaic_global = models.CharField(
        db_column='MOSAIC_GLOBAL', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    mosaicfactor1 = models.CharField(
        db_column='MOSAICFACTOR1', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    mosaicfactor2 = models.CharField(
        db_column='MOSAICFACTOR2', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    mosaicfactor3 = models.CharField(
        db_column='MOSAICFACTOR3', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    mosaicfactor4 = models.CharField(
        db_column='MOSAICFACTOR4', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    mosaicfactor5 = models.CharField(
        db_column='MOSAICFACTOR5', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    mosaic_origem = models.CharField(
        db_column='MOSAIC_ORIGEM', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    mother_score = models.CharField(
        db_column='MOTHER_SCORE', max_length=2, blank=True, null=True)
    nr_cpf = models.BigIntegerField(blank=True, null=True)
    # Field name made lowercase.
    origem_dado_topdados = models.CharField(
        db_column='ORIGEM_DADO_TOPDADOS', max_length=100)
    # Field name made lowercase.
    id_usuario_consultou = models.IntegerField(
        db_column='ID_USUARIO_CONSULTOU', blank=True, null=True)
    # Field name made lowercase.
    dt_sci_data_consulta = models.DateTimeField(
        db_column='DT_SCI_DATA_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    rg_data_emissao = models.CharField(
        db_column='RG_DATA_EMISSAO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    cnh = models.CharField(
        db_column='CNH', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    data_habilitacao = models.CharField(
        db_column='DATA_HABILITACAO', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    dt_alteracao = models.DateTimeField(
        db_column='DT_ALTERACAO', blank=True, null=True)
    # Field name made lowercase.
    id_usuario = models.IntegerField(
        db_column='ID_USUARIO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PESSOA_FISICA_HISTORICO_ALTERACAO'


class ProdutoresRurais(models.Model):
    # Field name made lowercase.
    produtores_rurais_id = models.AutoField(db_column='PRODUTORES_RURAIS_ID')
    # Field name made lowercase.
    contatos_id = models.IntegerField(
        db_column='CONTATOS_ID', blank=True, null=True)
    # Field name made lowercase.
    empresas_id = models.IntegerField(
        db_column='EMPRESAS_ID', blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    ie = models.BigIntegerField(db_column='IE', blank=True, null=True)
    # Field name made lowercase.
    cnae = models.CharField(
        db_column='CNAE', max_length=7, blank=True, null=True)
    # Field name made lowercase.
    status = models.BooleanField(db_column='STATUS', blank=True, null=True)
    # Field name made lowercase.
    protocolo = models.CharField(
        db_column='PROTOCOLO', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    data_consulta = models.DateTimeField(
        db_column='DATA_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    data_inclusao = models.DateTimeField(
        db_column='DATA_INCLUSAO', blank=True, null=True)
    # Field name made lowercase.
    data_atualizacao = models.DateTimeField(
        db_column='DATA_ATUALIZACAO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PRODUTORES_RURAIS'
        unique_together = (('contatos_id', 'empresas_id', 'uf', 'ie'),)


class Profissao(models.Model):
    # Field name made lowercase.
    ativ = models.CharField(db_column='ATIV', primary_key=True,
                            max_length=4, db_comment='- C¾digo da Atividade Profissi')
    # Field name made lowercase.
    descricao = models.CharField(
        db_column='DESCRICAO', max_length=70, db_comment='- Nome da Atividade Profission')
    # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=8,
                            db_comment='- Tipo da Atividade Profission')
    # Field name made lowercase.
    classe = models.CharField(db_column='CLASSE', max_length=8, blank=True,
                              null=True, db_comment='- Classe da Atividade Profissi')
    # Field name made lowercase.
    grupo = models.CharField(db_column='GRUPO', max_length=8, blank=True,
                             null=True, db_comment='- Grupo da Atividade Profissio')

    class Meta:
        managed = False
        db_table = 'PROFISSAO'


class ProvaveisEmail(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', blank=True, null=True)
    # Field name made lowercase.
    cpf = models.CharField(
        db_column='CPF', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    email = models.CharField(
        db_column='Email', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    id_email = models.BigIntegerField(
        db_column='ID_EMAIL', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PROVAVEIS_EMAIL'


class ProvaveisEndereco(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', blank=True, null=True)
    # Field name made lowercase.
    cpf = models.CharField(
        db_column='CPF', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    logradouro = models.CharField(
        db_column='Logradouro', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    bairro = models.CharField(
        db_column='Bairro', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    cidade = models.CharField(
        db_column='Cidade', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=500,
                          blank=True, null=True)
    # Field name made lowercase.
    cep = models.CharField(
        db_column='CEP', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    id_endereco = models.BigIntegerField(
        db_column='ID_ENDERECO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PROVAVEIS_ENDERECO'


class ProvaveisTelefone(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', blank=True, null=True)
    # Field name made lowercase.
    cpf = models.CharField(
        db_column='CPF', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    ddd = models.CharField(
        db_column='DDD', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    telefone = models.CharField(
        db_column='Telefone', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    id_telefone = models.BigIntegerField(
        db_column='ID_TELEFONE', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PROVAVEIS_TELEFONE'


class Relacionamento(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    cpf_relacionamento = models.TextField(
        db_column='CPF_RELACIONAMENTO', blank=True, null=True)
    # Field name made lowercase.
    nome = models.TextField(db_column='NOME', blank=True, null=True)
    # Field name made lowercase.
    vinculo = models.TextField(db_column='VINCULO', blank=True, null=True)
    # Field name made lowercase.
    id_usuario_consultou = models.IntegerField(
        db_column='ID_USUARIO_CONSULTOU', blank=True, null=True)
    # Field name made lowercase.
    dt_sci_data_consulta = models.DateTimeField(
        db_column='DT_SCI_DATA_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    origem_dado_topdados = models.CharField(
        db_column='ORIGEM_DADO_TOPDADOS', max_length=30)
    # Field name made lowercase.
    id_relacionamento = models.BigIntegerField(db_column='ID_RELACIONAMENTO')
    # Field name made lowercase.
    dt_nascimento = models.CharField(
        db_column='DT_NASCIMENTO', max_length=10, blank=True, null=True)
    dt_bigdata_data_consulta = models.DateTimeField(
        db_column='DT_BIGDATA_DATA_CONSULTA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RELACIONAMENTO'


class RepiccConsulta(models.Model):
    # Field name made lowercase.
    id_consulta = models.BigIntegerField(db_column='ID_CONSULTA')
    # Field name made lowercase.
    dt_consulta = models.DateTimeField(
        db_column='DT_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    ds_token = models.CharField(
        db_column='DS_TOKEN', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    nu_documento = models.CharField(db_column='NU_DOCUMENTO', max_length=14)
    # Field name made lowercase.
    ds_json_resultado = models.TextField(
        db_column='DS_JSON_RESULTADO', blank=True, null=True)
    # Field name made lowercase.
    ic_cadastral = models.CharField(db_column='IC_CADASTRAL', max_length=1)
    # Field name made lowercase.
    ic_obito = models.CharField(db_column='IC_OBITO', max_length=1)
    # Field name made lowercase.
    ic_erro = models.CharField(db_column='IC_ERRO', max_length=1)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(db_column='DT_INCLUSAO')
    # Field name made lowercase.
    ic_retorno_tratado = models.CharField(
        db_column='IC_RETORNO_TRATADO', max_length=1)
    # Field name made lowercase.
    id_usuario_consultou = models.IntegerField(
        db_column='ID_USUARIO_CONSULTOU', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'REPICC_CONSULTA'


class RepresLegal(models.Model):
    # Field name made lowercase.
    cnpj = models.CharField(
        db_column='CNPJ', max_length=14, blank=True, null=True)
    # Field name made lowercase.
    cpf_repres = models.CharField(
        db_column='CPF_REPRES', max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'REPRES_LEGAL'


class ResultadoComparacaoBases(models.Model):
    # Field name made lowercase.
    data = models.CharField(
        db_column='DATA', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    servidor = models.CharField(
        db_column='SERVIDOR', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    variavel = models.CharField(
        db_column='VARIAVEL', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    qtde = models.BigIntegerField(db_column='QTDE', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RESULTADO_COMPARACAO_BASES'


class SciConsulta(models.Model):
    # Field name made lowercase.
    id_consulta = models.BigIntegerField(db_column='ID_CONSULTA')
    # Field name made lowercase.
    dt_consulta = models.DateTimeField(
        db_column='DT_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    ds_token = models.CharField(
        db_column='DS_TOKEN', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    nu_documento = models.CharField(db_column='NU_DOCUMENTO', max_length=14)
    # Field name made lowercase.
    ds_json_resultado = models.TextField(
        db_column='DS_JSON_RESULTADO', blank=True, null=True)
    # Field name made lowercase.
    ic_cadastral = models.CharField(db_column='IC_CADASTRAL', max_length=1)
    # Field name made lowercase.
    ic_obito = models.CharField(db_column='IC_OBITO', max_length=1)
    # Field name made lowercase.
    ic_erro = models.CharField(db_column='IC_ERRO', max_length=1)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(db_column='DT_INCLUSAO')
    # Field name made lowercase.
    ic_retorno_tratado = models.CharField(
        db_column='IC_RETORNO_TRATADO', max_length=1)
    # Field name made lowercase.
    id_usuario_consultou = models.IntegerField(
        db_column='ID_USUARIO_CONSULTOU', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SCI_CONSULTA'


class SciConsultasDeParaItensOrdem(models.Model):
    # Field name made lowercase.
    ds_item = models.CharField(db_column='DS_ITEM', max_length=718)
    # Field name made lowercase.
    ordem = models.IntegerField(db_column='ORDEM', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SCI_CONSULTAS_DE_PARA_ITENS_ORDEM'


class SciConsultasRetornoCadastral(models.Model):
    # Field name made lowercase.
    id_consulta_fk = models.BigIntegerField(db_column='ID_CONSULTA_FK')
    # Field name made lowercase.
    nu_documento = models.CharField(db_column='NU_DOCUMENTO', max_length=14)
    # Field name made lowercase.
    dt_consulta = models.DateTimeField(
        db_column='DT_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    tipo_retorno = models.TextField(
        db_column='TIPO_RETORNO', blank=True, null=True)
    # Field name made lowercase.
    id_consulta = models.TextField(
        db_column='ID_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    cpf = models.TextField(db_column='CPF', blank=True, null=True)
    # Field name made lowercase.
    nome = models.TextField(db_column='NOME', blank=True, null=True)
    # Field name made lowercase.
    rg = models.TextField(db_column='RG', blank=True, null=True)
    # Field name made lowercase.
    rg_orgao_emissor = models.TextField(
        db_column='RG_ORGAO_EMISSOR', blank=True, null=True)
    # Field name made lowercase.
    rg_uf_emissao = models.TextField(
        db_column='RG_UF_EMISSAO', blank=True, null=True)
    # Field name made lowercase.
    rg_data_emissao = models.TextField(
        db_column='RG_DATA_EMISSAO', blank=True, null=True)
    # Field name made lowercase.
    dt_nascimento = models.TextField(
        db_column='DT_NASCIMENTO', blank=True, null=True)
    # Field name made lowercase.
    idade = models.TextField(db_column='IDADE', blank=True, null=True)
    # Field name made lowercase.
    signo = models.TextField(db_column='SIGNO', blank=True, null=True)
    # Field name made lowercase.
    sexo = models.TextField(db_column='SEXO', blank=True, null=True)
    # Field name made lowercase.
    mae = models.TextField(db_column='MAE', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SCI_CONSULTAS_RETORNO_CADASTRAL'


class SciConsultasRetornoEmail(models.Model):
    # Field name made lowercase.
    id_consulta_fk = models.BigIntegerField(db_column='ID_CONSULTA_FK')
    # Field name made lowercase.
    nu_documento = models.CharField(db_column='NU_DOCUMENTO', max_length=14)
    # Field name made lowercase.
    dt_consulta = models.DateTimeField(
        db_column='DT_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    email = models.TextField(db_column='EMAIL', blank=True, null=True)
    # Field name made lowercase.
    ranking = models.TextField(db_column='RANKING', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SCI_CONSULTAS_RETORNO_EMAIL'


class SciConsultasRetornoEndereco(models.Model):
    # Field name made lowercase.
    id_consulta_fk = models.BigIntegerField(db_column='ID_CONSULTA_FK')
    # Field name made lowercase.
    nu_documento = models.CharField(db_column='NU_DOCUMENTO', max_length=14)
    # Field name made lowercase.
    dt_consulta = models.DateTimeField(
        db_column='DT_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    bairro = models.TextField(db_column='BAIRRO', blank=True, null=True)
    # Field name made lowercase.
    cep = models.TextField(db_column='CEP', blank=True, null=True)
    # Field name made lowercase.
    cidade = models.TextField(db_column='CIDADE', blank=True, null=True)
    # Field name made lowercase.
    complemento = models.TextField(
        db_column='COMPLEMENTO', blank=True, null=True)
    # Field name made lowercase.
    data = models.TextField(db_column='DATA', blank=True, null=True)
    # Field name made lowercase.
    ddd = models.TextField(db_column='DDD', blank=True, null=True)
    # Field name made lowercase.
    latitude = models.TextField(db_column='LATITUDE', blank=True, null=True)
    # Field name made lowercase.
    logradouro = models.TextField(
        db_column='LOGRADOURO', blank=True, null=True)
    # Field name made lowercase.
    longitude = models.TextField(db_column='LONGITUDE', blank=True, null=True)
    # Field name made lowercase.
    numero = models.TextField(db_column='NUMERO', blank=True, null=True)
    # Field name made lowercase.
    ranking = models.TextField(db_column='RANKING', blank=True, null=True)
    # Field name made lowercase.
    uf = models.TextField(db_column='UF', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SCI_CONSULTAS_RETORNO_ENDERECO'


class SciConsultasRetornoRelacionamento(models.Model):
    # Field name made lowercase.
    id_consulta_fk = models.BigIntegerField(db_column='ID_CONSULTA_FK')
    # Field name made lowercase.
    nu_documento = models.CharField(db_column='NU_DOCUMENTO', max_length=14)
    # Field name made lowercase.
    dt_consulta = models.DateTimeField(
        db_column='DT_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    data = models.TextField(db_column='DATA', blank=True, null=True)
    # Field name made lowercase.
    cpf = models.TextField(db_column='CPF', blank=True, null=True)
    # Field name made lowercase.
    nome = models.TextField(db_column='NOME', blank=True, null=True)
    # Field name made lowercase.
    relacionamento = models.TextField(
        db_column='RELACIONAMENTO', blank=True, null=True)
    # Field name made lowercase.
    vinculo = models.TextField(db_column='VINCULO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SCI_CONSULTAS_RETORNO_RELACIONAMENTO'


class SciConsultasRetornoTelefone(models.Model):
    # Field name made lowercase.
    id_consulta_fk = models.BigIntegerField(db_column='ID_CONSULTA_FK')
    # Field name made lowercase.
    nu_documento = models.CharField(db_column='NU_DOCUMENTO', max_length=14)
    # Field name made lowercase.
    dt_consulta = models.DateTimeField(
        db_column='DT_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    ddd = models.TextField(db_column='DDD', blank=True, null=True)
    # Field name made lowercase.
    telefone = models.TextField(db_column='TELEFONE', blank=True, null=True)
    # Field name made lowercase.
    tipo = models.TextField(db_column='TIPO', blank=True, null=True)
    # Field name made lowercase.
    operadora = models.TextField(db_column='OPERADORA', blank=True, null=True)
    # Field name made lowercase.
    ranking = models.TextField(db_column='RANKING', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SCI_CONSULTAS_RETORNO_TELEFONE'


class SciConsultasTratadas(models.Model):
    id = models.BigIntegerField(db_column='ID')  # Field name made lowercase.
    # Field name made lowercase.
    id_pai_fk = models.BigIntegerField(
        db_column='ID_PAI_FK', blank=True, null=True)
    # Field name made lowercase.
    id_consulta_fk = models.IntegerField(db_column='ID_CONSULTA_FK')
    # Field name made lowercase.
    ds_key = models.CharField(db_column='DS_KEY', max_length=100)
    # Field name made lowercase.
    ds_value = models.TextField(db_column='DS_VALUE', blank=True, null=True)
    # Field name made lowercase.
    ds_type = models.CharField(db_column='DS_TYPE', max_length=10)
    # Field name made lowercase.
    ic_tratado = models.CharField(db_column='IC_TRATADO', max_length=1)

    class Meta:
        managed = False
        db_table = 'SCI_CONSULTAS_TRATADAS'


class SciToken(models.Model):
    # Field name made lowercase.
    id_token = models.IntegerField(db_column='ID_TOKEN')
    # Field name made lowercase.
    dt_data_token = models.DateTimeField(db_column='DT_DATA_TOKEN')
    # Field name made lowercase.
    ds_token = models.CharField(db_column='DS_TOKEN', max_length=100)

    class Meta:
        managed = False
        db_table = 'SCI_TOKEN'


class SituacaoCadastralPf(models.Model):
    # Field name made lowercase.
    cd_sit_cad = models.SmallIntegerField(
        db_column='CD_SIT_CAD', db_comment='- C¾digo da SituaþÒo Cadastral')
    # Field name made lowercase.
    ds_sit_cad = models.CharField(
        db_column='DS_SIT_CAD', max_length=35, db_comment='- Nome da SituaþÒo Cadastral d')
    # Field name made lowercase.
    id_sit_cad = models.SmallIntegerField(db_column='ID_SIT_CAD')

    class Meta:
        managed = False
        db_table = 'SITUACAO_CADASTRAL_PF'


class SituacaoEspecial(models.Model):
    # Field name made lowercase.
    id_sit_esp = models.SmallAutoField(
        db_column='ID_SIT_ESP', primary_key=True, db_comment='- C¾digo Interno Sequencial da')
    # Field name made lowercase.
    ds_sit_esp = models.CharField(db_column='DS_SIT_ESP', max_length=70,
                                  blank=True, null=True, db_comment='- Nome da SituaþÒo Especial da')

    class Meta:
        managed = False
        db_table = 'SITUACAO_ESPECIAL'


class Socios(models.Model):
    # Field name made lowercase.
    empresas_id = models.IntegerField(
        db_column='EMPRESAS_ID', blank=True, null=True)
    # Field name made lowercase.
    tp_socio_id = models.SmallIntegerField(
        db_column='TP_SOCIO_ID', blank=True, null=True)
    # Field name made lowercase.
    empresas_id_socio = models.IntegerField(
        db_column='EMPRESAS_ID_SOCIO', blank=True, null=True)
    # Field name made lowercase.
    contatos_id_socio = models.BigIntegerField(
        db_column='CONTATOS_ID_SOCIO', blank=True, null=True)
    # Field name made lowercase.
    participacao_socio = models.DecimalField(
        db_column='PARTICIPACAO_SOCIO', max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SOCIOS'


class TabelasValidacaoIndices(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    # Field name made lowercase.
    servidor = models.CharField(db_column='SERVIDOR', max_length=100)
    # Field name made lowercase.
    banco = models.CharField(db_column='BANCO', max_length=100)
    # Field name made lowercase.
    tabela = models.CharField(db_column='TABELA', max_length=255)
    # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=100)

    class Meta:
        managed = False
        db_table = 'TABELAS_VALIDACAO_INDICES'


class TbBolsaFamiliaDep(models.Model):
    # Field name made lowercase.
    nome = models.CharField(
        db_column='NOME', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    nasc = models.DateTimeField(db_column='NASC', blank=True, null=True)
    # Field name made lowercase.
    sexo = models.CharField(
        db_column='SEXO', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    cidade = models.CharField(
        db_column='CIDADE', max_length=40, blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    cpf_resp = models.CharField(
        db_column='CPF_RESP', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    num_nis_resp = models.CharField(
        db_column='NUM_NIS_RESP', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    des_situacao = models.CharField(
        db_column='DES_SITUACAO', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    status_beneficio = models.CharField(
        db_column='STATUS_BENEFICIO', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    mes_situacao = models.CharField(
        db_column='MES_SITUACAO', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    ano_situacao = models.CharField(
        db_column='ANO_SITUACAO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    cpf_dep = models.CharField(
        db_column='CPF_DEP', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    origem_cpf = models.CharField(
        db_column='ORIGEM_CPF', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    cadastro_id = models.IntegerField(
        db_column='CADASTRO_ID', blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_BOLSA_FAMILIA_DEP'


class TbBolsaFamiliaResp(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', blank=True, null=True)
    # Field name made lowercase.
    cpf = models.CharField(
        db_column='CPF', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    nome = models.CharField(
        db_column='NOME', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    nasc = models.DateTimeField(db_column='NASC', blank=True, null=True)
    # Field name made lowercase.
    sexo = models.CharField(
        db_column='SEXO', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    cidade = models.CharField(
        db_column='CIDADE', max_length=40, blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    nr_dependentes = models.IntegerField(
        db_column='NR_DEPENDENTES', blank=True, null=True)
    # Field name made lowercase.
    num_nis = models.CharField(
        db_column='NUM_NIS', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    des_situacao = models.CharField(
        db_column='DES_SITUACAO', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    status_beneficio = models.CharField(
        db_column='STATUS_BENEFICIO', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    mes_situacao = models.CharField(
        db_column='MES_SITUACAO', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    valor_beneficio = models.CharField(
        db_column='VALOR_BENEFICIO', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    titulo_eleitor = models.CharField(
        db_column='TITULO_ELEITOR', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    atrib_tit_eleitor = models.SmallIntegerField(
        db_column='ATRIB_TIT_ELEITOR', blank=True, null=True)
    # Field name made lowercase.
    origem_cpf = models.CharField(
        db_column='ORIGEM_CPF', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    ano_situacao = models.CharField(
        db_column='ANO_SITUACAO', max_length=4, blank=True, null=True)
    # Field name made lowercase.
    cadastro_id = models.IntegerField(
        db_column='CADASTRO_ID', blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_BOLSA_FAMILIA_RESP'


class TbCartaoMastercard(models.Model):
    # Field name made lowercase.
    empresas_id = models.IntegerField(db_column='EMPRESAS_ID', unique=True)
    # Field name made lowercase.
    classoper = models.IntegerField(db_column='CLASSOPER')
    # Field name made lowercase.
    classoper_desc = models.CharField(
        db_column='CLASSOPER_DESC', max_length=36)
    # Field name made lowercase.
    flag_pump = models.IntegerField(db_column='FLAG_PUMP')
    # Field name made lowercase.
    flag_cashback = models.IntegerField(db_column='FLAG_CASHBACK')
    # Field name made lowercase.
    flag_nfc = models.IntegerField(db_column='FLAG_NFC')
    # Field name made lowercase.
    flag_0d = models.IntegerField(db_column='FLAG_0D')
    # Field name made lowercase.
    ultima_operacao = models.CharField(
        db_column='ULTIMA_OPERACAO', max_length=4, blank=True, null=True)
    # Field name made lowercase.
    tp_distribuicao = models.IntegerField(db_column='TP_DISTRIBUICAO')
    # Field name made lowercase.
    tp_distribuicao_desc = models.CharField(
        db_column='TP_DISTRIBUICAO_DESC', max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_CARTAO_MASTERCARD'


class TbClassServPublicos(models.Model):
    # Field name made lowercase.
    federal = models.CharField(
        db_column='FEDERAL', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    militar = models.CharField(
        db_column='MILITAR', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    estadual = models.CharField(
        db_column='ESTADUAL', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    municipal = models.CharField(
        db_column='MUNICIPAL', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    cod_final = models.CharField(
        db_column='COD_FINAL', max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_CLASS_SERV_PUBLICOS'


class TbCnesPj(models.Model):
    dt_cadastro = models.CharField(max_length=255, blank=True, null=True)
    # Field name made lowercase.
    dd_atualiza = models.CharField(
        db_column='DD_ATUALIZA', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    dt_atualiza_local = models.CharField(
        db_column='DT_ATUALIZA_LOCAL', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    nome = models.CharField(
        db_column='NOME', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    cnes = models.CharField(
        db_column='CNES', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    cod_municipio_ibge = models.CharField(
        db_column='COD_MUNICIPIO_IBGE', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    nu_cnpj_mantenedora = models.CharField(
        db_column='NU_CNPJ_MANTENEDORA', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    razao_social_mantenedora = models.CharField(
        db_column='RAZAO_SOCIAL_MANTENEDORA', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    nome_empresarial = models.CharField(
        db_column='NOME_EMPRESARIAL', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    nome_fantasia = models.CharField(
        db_column='NOME_FANTASIA', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    tipo_estabelecimento = models.CharField(
        db_column='TIPO_ESTABELECIMENTO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    gestao = models.CharField(
        db_column='GESTAO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    cnpj = models.CharField(
        db_column='CNPJ', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    rsocial = models.CharField(
        db_column='RSOCIAL', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    cpf = models.CharField(
        db_column='CPF', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    personalidade = models.CharField(
        db_column='PERSONALIDADE', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    tipo = models.CharField(
        db_column='TIPO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    endereco = models.CharField(
        db_column='ENDERECO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    num = models.CharField(
        db_column='NUM', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    compl = models.CharField(
        db_column='COMPL', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    bairro = models.CharField(
        db_column='BAIRRO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    cep = models.CharField(
        db_column='CEP', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    cidade = models.CharField(
        db_column='CIDADE', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=255,
                          blank=True, null=True)
    # Field name made lowercase.
    telefone = models.CharField(
        db_column='TELEFONE', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    tipo_de_estabelecimento = models.CharField(
        db_column='TIPO_DE_ESTABELECIMENTO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    sub_tipo_de_estabelecimento = models.CharField(
        db_column='SUB_TIPO_DE_ESTABELECIMENTO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    dependencia = models.CharField(
        db_column='DEPENDENCIA', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    numero_alvara = models.CharField(
        db_column='NUMERO_ALVARA', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    orgao_expedidor = models.CharField(
        db_column='ORGAO_EXPEDIDOR', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    dt_expedicao = models.CharField(
        db_column='DT_EXPEDICAO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    horario_de_funcionamento = models.CharField(
        db_column='HORARIO_DE_FUNCIONAMENTO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    razao_social_atribuido = models.CharField(
        db_column='RAZAO_SOCIAL_ATRIBUIDO', max_length=155, blank=True, null=True)
    # Field name made lowercase.
    razao_social = models.CharField(
        db_column='RAZAO_SOCIAL', max_length=155, blank=True, null=True)
    # Field name made lowercase.
    cnpj_atribuido = models.CharField(
        db_column='CNPJ_ATRIBUIDO', max_length=14, blank=True, null=True)
    # Field name made lowercase.
    empresas_id = models.BigIntegerField(
        db_column='EMPRESAS_ID', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id = models.IntegerField(
        db_column='CADASTRO_ID', blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)
    # Field name made lowercase.
    dt_atualizacao = models.DateTimeField(
        db_column='DT_ATUALIZACAO', blank=True, null=True)
    # Field name made lowercase.
    email = models.CharField(
        db_column='EMAIL', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    conexao_in = models.CharField(
        db_column='CONEXAO_IN', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_CNES_PJ'


class TbCnesProfissionais(models.Model):
    # Field name made lowercase.
    cnes_profissionais_id = models.BigAutoField(
        db_column='CNES_PROFISSIONAIS_ID')
    # Field name made lowercase.
    contatos_id = models.IntegerField(
        db_column='CONTATOS_ID', blank=True, null=True)
    # Field name made lowercase.
    cns = models.BigIntegerField(db_column='CNS', blank=True, null=True)
    # Field name made lowercase.
    cnes = models.IntegerField(db_column='CNES', blank=True, null=True)
    # Field name made lowercase.
    cd_cbo = models.IntegerField(db_column='CD_CBO', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id = models.IntegerField(
        db_column='CADASTRO_ID', blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)
    # Field name made lowercase.
    estabelecimento = models.CharField(
        db_column='ESTABELECIMENTO', max_length=200, blank=True, null=True)
    empresas_id_estabelecimento = models.IntegerField(
        db_column='EMPRESAS_ID_ESTABELECIMENTO', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    tipo = models.CharField(
        db_column='TIPO', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    cnpj_estabelecimento = models.CharField(
        db_column='CNPJ_ESTABELECIMENTO', max_length=14, blank=True, null=True)
    # Field name made lowercase.
    empresas_id = models.IntegerField(
        db_column='EMPRESAS_ID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_CNES_PROFISSIONAIS'


class TbCns(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=11)
    # Field name made lowercase.
    cns = models.CharField(
        db_column='CNS', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    pis = models.CharField(
        db_column='PIS', max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_CNS'


class TbConselhos(models.Model):
    # Field name made lowercase.
    contatos_id = models.CharField(
        db_column='CONTATOS_ID', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    nome = models.CharField(
        db_column='NOME', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    numero_identidade = models.CharField(
        db_column='NUMERO_IDENTIDADE', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    situacao = models.CharField(
        db_column='SITUACAO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    especialidade_categoria = models.CharField(
        db_column='ESPECIALIDADE_CATEGORIA', max_length=600, blank=True, null=True)
    # Field name made lowercase.
    tp_identidade = models.CharField(db_column='TP_IDENTIDADE', max_length=4)
    # Field name made lowercase.
    dt_inclusao = models.CharField(db_column='DT_INCLUSAO', max_length=10)
    # Field name made lowercase.
    tipo_inscricao = models.CharField(
        db_column='TIPO_INSCRICAO', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    outras_inscricoes = models.CharField(
        db_column='OUTRAS_INSCRICOES', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    conselho_orgao = models.CharField(
        db_column='CONSELHO_ORGAO', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    estado = models.CharField(
        db_column='ESTADO', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    registro = models.CharField(
        db_column='REGISTRO', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    especialidade_tratada = models.CharField(
        db_column='ESPECIALIDADE_TRATADA', max_length=1000, blank=True, null=True)
    # Field name made lowercase.
    cbo_atribuido = models.CharField(
        db_column='CBO_ATRIBUIDO', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    tipo_cbo = models.CharField(
        db_column='TIPO_CBO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    descricao = models.CharField(
        db_column='DESCRICAO', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_CONSELHOS'


class TbCreditTarget(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    credit_target = models.CharField(
        db_column='CREDIT_TARGET', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(db_column='DT_INCLUSAO')
    # Field name made lowercase.
    dt_atualizacao = models.DateTimeField(
        db_column='DT_ATUALIZACAO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_CREDIT_TARGET'


class TbCtps(models.Model):
    # Field name made lowercase.
    ctps_id = models.BigIntegerField(
        db_column='CTPS_ID', unique=True, blank=True, null=True)
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    numero_ctps = models.CharField(
        db_column='NUMERO_CTPS', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    serie_ctps = models.CharField(
        db_column='SERIE_CTPS', max_length=7, blank=True, null=True)
    # Field name made lowercase.
    dt_emissao_ctps = models.CharField(
        db_column='DT_EMISSAO_CTPS', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    uf_emissao_ctps = models.CharField(
        db_column='UF_EMISSAO_CTPS', max_length=3, blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_CTPS'


class TbEmpregos(models.Model):
    # Field name made lowercase.
    empregos_id = models.BigIntegerField(
        db_column='EMPREGOS_ID', unique=True, blank=True, null=True)
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    cpf = models.CharField(
        db_column='CPF', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    nome = models.CharField(
        db_column='NOME', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    razao_social = models.CharField(
        db_column='RAZAO_SOCIAL', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    tipo = models.CharField(
        db_column='TIPO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    doc = models.CharField(
        db_column='DOC', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    remuneracao = models.DecimalField(
        db_column='REMUNERACAO', max_digits=8, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    cbo = models.CharField(
        db_column='CBO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)
    # Field name made lowercase.
    dt_inicio = models.CharField(
        db_column='DT_INICIO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    dt_termino = models.CharField(
        db_column='DT_TERMINO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    origem_dado = models.CharField(
        db_column='ORIGEM_DADO', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_EMPREGOS'


class TbEscolaridade(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', unique=True, blank=True, null=True)
    # Field name made lowercase.
    escolaridade = models.CharField(
        db_column='ESCOLARIDADE', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    origem_esc = models.CharField(db_column='ORIGEM_ESC', max_length=13)
    # Field name made lowercase.
    conselho_orgao = models.CharField(
        db_column='CONSELHO_ORGAO', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_ESCOLARIDADE'


class TbExpImp(models.Model):
    # Field name made lowercase.
    empresas_id = models.IntegerField(db_column='EMPRESAS_ID')
    # Field name made lowercase.
    cnpj = models.CharField(
        db_column='CNPJ', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    fx_valor_exp_imp = models.CharField(
        db_column='FX_VALOR_EXP_IMP', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=3)
    # Field name made lowercase.
    periodo = models.CharField(
        db_column='PERIODO', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_EXP_IMP'


class TbFgts(models.Model):
    # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', unique=True,
                           max_length=255, blank=True, null=True)
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', unique=True, blank=True, null=True)
    # Field name made lowercase.
    pis = models.CharField(
        db_column='PIS', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    ano_base = models.IntegerField(db_column='ANO_BASE', blank=True, null=True)
    # Field name made lowercase.
    flag_2017 = models.IntegerField(db_column='FLAG_2017')
    # Field name made lowercase.
    flag_2018 = models.IntegerField(db_column='FLAG_2018')
    # Field name made lowercase.
    cadastro_id = models.IntegerField(db_column='CADASTRO_ID')
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(db_column='DT_INCLUSAO')

    class Meta:
        managed = False
        db_table = 'TB_FGTS'


class TbHhMs(models.Model):
    # Field name made lowercase.
    household_id = models.BigIntegerField(
        db_column='HOUSEHOLD_ID', blank=True, null=True)
    historico_enderecos_id = models.BigIntegerField(
        db_column='HISTORICO_ENDERECOS_ID', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    flag_presenca_criancas = models.BooleanField(
        db_column='FLAG_PRESENCA_CRIANCAS', blank=True, null=True)
    # Field name made lowercase.
    tempo_residencia_id = models.SmallIntegerField(
        db_column='TEMPO_RESIDENCIA_ID', blank=True, null=True)
    # Field name made lowercase.
    tipo_familia_id = models.SmallIntegerField(
        db_column='TIPO_FAMILIA_ID', blank=True, null=True)
    # Field name made lowercase.
    qtd_pessoas = models.SmallIntegerField(
        db_column='QTD_PESSOAS', blank=True, null=True)
    faixa_renda_household_id = models.SmallIntegerField(
        db_column='FAIXA_RENDA_HOUSEHOLD_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TB_HH_MS'


class TbHhMs2014(models.Model):
    # Field name made lowercase.
    household_id_2014 = models.IntegerField(db_column='HOUSEHOLD_ID_2014')
    # Field name made lowercase.
    match_end = models.CharField(db_column='MATCH_END', max_length=50)
    # Field name made lowercase.
    qtde_pessoas_household = models.IntegerField(
        db_column='QTDE_PESSOAS_HOUSEHOLD')
    # Field name made lowercase.
    faixa_renda_household_id = models.IntegerField(
        db_column='FAIXA_RENDA_HOUSEHOLD_ID')
    # Field name made lowercase.
    origem = models.CharField(db_column='ORIGEM', max_length=36)

    class Meta:
        managed = False
        db_table = 'TB_HH_MS_2014'


class TbHhMs2016(models.Model):
    # Field name made lowercase.
    household_id_2016 = models.IntegerField(db_column='HOUSEHOLD_ID_2016')
    # Field name made lowercase.
    match_end = models.CharField(
        db_column='MATCH_END', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    origem = models.CharField(db_column='ORIGEM', max_length=15)
    # Field name made lowercase.
    qtde_pessoas_household = models.IntegerField(
        db_column='QTDE_PESSOAS_HOUSEHOLD', blank=True, null=True)
    # Field name made lowercase.
    faixa_renda_household_id = models.IntegerField(
        db_column='FAIXA_RENDA_HOUSEHOLD_ID')

    class Meta:
        managed = False
        db_table = 'TB_HH_MS_2016'


class TbMedicos(models.Model):
    # Field name made lowercase.
    medicos_id = models.IntegerField(db_column='MEDICOS_ID')
    # Field name made lowercase.
    contatos_id = models.IntegerField(
        db_column='CONTATOS_ID', blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)
    # Field name made lowercase.
    dt_atualizacao = models.DateTimeField(
        db_column='DT_ATUALIZACAO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_MEDICOS'


class TbMinhaCasaMinhaVida(models.Model):
    # Field name made lowercase.
    cpf = models.CharField(
        db_column='CPF', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', blank=True, null=True)
    # Field name made lowercase.
    dt_consulta = models.DateField(
        db_column='DT_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id = models.CharField(db_column='CADASTRO_ID', max_length=4)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(db_column='DT_INCLUSAO')

    class Meta:
        managed = False
        db_table = 'TB_MINHA_CASA_MINHA_VIDA'


class TbNis(models.Model):
    # Field name made lowercase.
    contatos_id = models.IntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    nis = models.BigIntegerField(db_column='NIS', blank=True, null=True)
    # Field name made lowercase.
    chave = models.CharField(
        db_column='CHAVE', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    cadastro_id = models.IntegerField(
        db_column='CADASTRO_ID', blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_NIS'


class TbPepTitularRelacionado(models.Model):
    # Field name made lowercase.
    cpf_titular = models.CharField(
        db_column='CPF_TITULAR', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    cpf_relacionado = models.CharField(
        db_column='CPF_RELACIONADO', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    nome_titular = models.CharField(
        db_column='NOME_TITULAR', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    nome_relacionado = models.CharField(
        db_column='NOME_RELACIONADO', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    relacionamento = models.CharField(
        db_column='RELACIONAMENTO', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    prioridade = models.IntegerField(
        db_column='PRIORIDADE', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_PEP_TITULAR_RELACIONADO'


class TbPis(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    pis = models.CharField(
        db_column='PIS', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    cadastro_id = models.BigIntegerField(
        db_column='CADASTRO_ID', blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateField(
        db_column='DT_INCLUSAO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_PIS'


class TbProfissao(models.Model):
    # Field name made lowercase.
    id_profissao = models.IntegerField(db_column='ID_PROFISSAO')
    # Field name made lowercase.
    cod_profissao = models.CharField(
        db_column='COD_PROFISSAO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    descricao_profissao = models.CharField(
        db_column='DESCRICAO_PROFISSAO', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    cadastro_id = models.IntegerField(db_column='CADASTRO_ID')
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)
    # Field name made lowercase.
    incremento = models.IntegerField(
        db_column='INCREMENTO', blank=True, null=True)
    # Field name made lowercase.
    atualizacao = models.IntegerField(
        db_column='ATUALIZACAO', blank=True, null=True)
    # Field name made lowercase.
    cbo_inexistente = models.IntegerField(
        db_column='CBO_INEXISTENTE', blank=True, null=True)
    # Field name made lowercase.
    profissao_igual = models.IntegerField(
        db_column='PROFISSAO_IGUAL', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_PROFISSAO'


class TbRegiaoBrasil(models.Model):
    # Field name made lowercase.
    regiao = models.CharField(
        db_column='Regiao', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    estado = models.CharField(
        db_column='Estado', max_length=25, blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    capital = models.CharField(
        db_column='Capital', max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_REGIAO_BRASIL'


class TbServidoresPublicos(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', blank=True, null=True)
    # Field name made lowercase.
    cpf = models.CharField(
        db_column='CPF', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    nome = models.CharField(
        db_column='NOME', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    descricao_cargo = models.CharField(
        db_column='DESCRICAO_CARGO', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    org_lotacao = models.CharField(
        db_column='ORG_LOTACAO', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    org_exercicio = models.CharField(
        db_column='ORG_EXERCICIO', max_length=250, blank=True, null=True)
    # Field name made lowercase.
    renda_bruta = models.DecimalField(
        db_column='RENDA_BRUTA', max_digits=10, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    serv_pb = models.CharField(
        db_column='SERV_PB', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    uf_portal = models.CharField(
        db_column='UF_PORTAL', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)
    # Field name made lowercase.
    obs = models.CharField(
        db_column='OBS', max_length=700, blank=True, null=True)
    # Field name made lowercase.
    afastamento = models.CharField(
        db_column='AFASTAMENTO', max_length=3, blank=True, null=True)
    # Field name made lowercase.
    vinculo = models.CharField(
        db_column='VINCULO', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    cadastro_id = models.IntegerField(
        db_column='CADASTRO_ID', blank=True, null=True)
    # Field name made lowercase.
    funcao = models.CharField(
        db_column='FUNCAO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    situacao = models.CharField(
        db_column='SITUACAO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    referencia = models.CharField(
        db_column='REFERENCIA', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    orgsup_lotacao = models.CharField(
        db_column='ORGSUP_LOTACAO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    faixa_salarial = models.CharField(
        db_column='FAIXA_SALARIAL', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    total_honorarios = models.IntegerField(
        db_column='TOTAL_HONORARIOS', blank=True, null=True)
    # Field name made lowercase.
    ultima_atualizacao_forn = models.DateTimeField(
        db_column='ULTIMA_ATUALIZACAO_FORN', blank=True, null=True)
    # Field name made lowercase.
    cbo_atribuido = models.CharField(
        db_column='CBO_ATRIBUIDO', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    seq_cpf = models.BigIntegerField(
        db_column='SEQ_CPF', blank=True, null=True)
    # Field name made lowercase.
    tipo_cbo = models.CharField(
        db_column='TIPO_CBO', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_SERVIDORES_PUBLICOS'


class TbSetorIbge(models.Model):
    # Field name made lowercase.
    cod_setor = models.CharField(
        db_column='COD_SETOR', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    cpf_dig = models.CharField(
        db_column='CPF_DIG', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    tipo_domicilio = models.CharField(
        db_column='TIPO_DOMICILIO', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    condicao_domicilio = models.CharField(
        db_column='CONDICAO_DOMICILIO', max_length=9, blank=True, null=True)
    # Field name made lowercase.
    chefe_familia = models.CharField(
        db_column='CHEFE_FAMILIA', max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_SETOR_IBGE'


class TbTse(models.Model):
    # Field name made lowercase.
    contatos_id = models.IntegerField(
        db_column='CONTATOS_ID', blank=True, null=True)
    # Field name made lowercase.
    titulo_eleitor = models.CharField(
        db_column='TITULO_ELEITOR', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    zona = models.CharField(
        db_column='ZONA', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    secao = models.CharField(
        db_column='SECAO', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_TSE'


class TbUniversitarios(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    nome = models.CharField(
        db_column='NOME', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    ano_vestibular = models.CharField(
        db_column='ANO_VESTIBULAR', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    faculdade = models.CharField(
        db_column='FACULDADE', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=255,
                          blank=True, null=True)
    # Field name made lowercase.
    campus = models.CharField(
        db_column='CAMPUS', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    curso = models.CharField(
        db_column='CURSO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    periodo_cursado = models.CharField(
        db_column='PERIODO_CURSADO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    inscricao_vestibular = models.CharField(
        db_column='INSCRICAO_VESTIBULAR', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    data_nascimento = models.CharField(
        db_column='DATA_NASCIMENTO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    cota = models.CharField(
        db_column='COTA', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    ano_conculsao = models.CharField(
        db_column='ANO_CONCULSAO', max_length=4, blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id = models.IntegerField(
        db_column='CADASTRO_ID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TB_UNIVERSITARIOS'


class Telefone(models.Model):
    # Field name made lowercase.
    historico_telefones_id = models.BigIntegerField(
        db_column='HISTORICO_TELEFONES_ID')
    # Field name made lowercase.
    historico_enderecos_id = models.BigIntegerField(
        db_column='HISTORICO_ENDERECOS_ID')
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    ddd = models.CharField(db_column='DDD', max_length=2)
    # Field name made lowercase.
    telefone = models.CharField(db_column='TELEFONE', max_length=9)
    # Field name made lowercase.
    tipo_telefone = models.SmallIntegerField(db_column='TIPO_TELEFONE')
    # Field name made lowercase.
    cadastro_id = models.IntegerField(db_column='CADASTRO_ID')
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)
    # Field name made lowercase.
    dt_atualizacao = models.DateTimeField(
        db_column='DT_ATUALIZACAO', blank=True, null=True)
    # Field name made lowercase.
    fone_nota = models.CharField(
        db_column='FONE_NOTA', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    dt_informacao = models.DateTimeField(
        db_column='DT_INFORMACAO', blank=True, null=True)
    # Field name made lowercase.
    sigilo = models.SmallIntegerField(
        db_column='SIGILO', blank=True, null=True)
    # Field name made lowercase.
    nsu = models.CharField(
        db_column='NSU', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    origem_serasa = models.CharField(
        db_column='ORIGEM_SERASA', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    prioridade = models.IntegerField(
        db_column='PRIORIDADE', blank=True, null=True)
    # Field name made lowercase.
    classificacao = models.CharField(
        db_column='CLASSIFICACAO', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    fonte_name = models.CharField(
        db_column='FONTE_NAME', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    dt_metralhadora = models.DateTimeField(
        db_column='DT_METRALHADORA', blank=True, null=True)
    # Field name made lowercase.
    origem_dado_topdados = models.CharField(
        db_column='ORIGEM_DADO_TOPDADOS', max_length=100)
    # Field name made lowercase.
    id_usuario_consultou = models.IntegerField(
        db_column='ID_USUARIO_CONSULTOU', blank=True, null=True)
    # Field name made lowercase.
    dt_sci_data_consulta = models.DateTimeField(
        db_column='DT_SCI_DATA_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    negativado = models.BooleanField(
        db_column='NEGATIVADO', blank=True, null=True)
    dt_bigdata_data_consulta = models.DateTimeField(
        db_column='DT_BIGDATA_DATA_CONSULTA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TELEFONE'


class TelefonesBloqueadosCompleto(models.Model):
    # Field name made lowercase.
    telefones_bloqueados_id = models.AutoField(
        db_column='TELEFONES_BLOQUEADOS_ID', primary_key=True)
    # Field name made lowercase.
    telefone = models.CharField(db_column='TELEFONE', max_length=8)
    # Field name made lowercase.
    ddd = models.CharField(db_column='DDD', max_length=2)
    # Field name made lowercase.
    dt_cadastro = models.DateTimeField(
        db_column='DT_CADASTRO', blank=True, null=True)
    # Field name made lowercase.
    dt_limite = models.DateTimeField(
        db_column='DT_LIMITE', blank=True, null=True)
    # Field name made lowercase.
    evento = models.CharField(
        db_column='EVENTO', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)
    # Field name made lowercase.
    arquivo = models.CharField(
        db_column='ARQUIVO', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)
    # Field name made lowercase. Field renamed because of name conflict.
    telefones_bloqueados_id_0 = models.AutoField(
        db_column='TELEFONES_BLOQUEADOS_ID', primary_key=True)
    # Field name made lowercase. Field renamed because of name conflict.
    telefone_0 = models.CharField(
        db_column='TELEFONE', max_length=9, blank=True, null=True)
    # Field name made lowercase. Field renamed because of name conflict.
    ddd_0 = models.CharField(db_column='DDD', max_length=2)
    # Field name made lowercase. Field renamed because of name conflict.
    dt_cadastro_0 = models.DateTimeField(
        db_column='DT_CADASTRO', blank=True, null=True)
    # Field name made lowercase. Field renamed because of name conflict.
    dt_limite_0 = models.DateTimeField(
        db_column='DT_LIMITE', blank=True, null=True)
    # Field name made lowercase. Field renamed because of name conflict.
    evento_0 = models.CharField(
        db_column='EVENTO', max_length=20, blank=True, null=True)
    # Field name made lowercase. Field renamed because of name conflict.
    dt_inclusao_0 = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)
    # Field name made lowercase. Field renamed because of name conflict.
    arquivo_0 = models.CharField(
        db_column='ARQUIVO', max_length=100, blank=True, null=True)
    # Field name made lowercase. Field renamed because of name conflict.
    uf_0 = models.CharField(
        db_column='UF', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    municipio = models.CharField(
        db_column='MUNICIPIO', max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TELEFONES_BLOQUEADOS_COMPLETO'


class TelefonesPublicos(models.Model):
    # Field name made lowercase.
    ddd = models.CharField(db_column='DDD', max_length=2,
                           blank=True, null=True)
    # Field name made lowercase.
    telefone = models.CharField(
        db_column='TELEFONE', max_length=9, blank=True, null=True)
    # Field name made lowercase.
    dt_ativacao = models.DateTimeField(
        db_column='DT_ATIVACAO', blank=True, null=True)
    # Field name made lowercase.
    match_end = models.CharField(
        db_column='MATCH_END', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    endereco = models.CharField(
        db_column='ENDERECO', max_length=130, blank=True, null=True)
    # Field name made lowercase.
    logr_tipo = models.CharField(
        db_column='LOGR_TIPO', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    logr_titulo = models.CharField(
        db_column='LOGR_TITULO', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    logr_nome = models.CharField(
        db_column='LOGR_NOME', max_length=60, blank=True, null=True)
    # Field name made lowercase.
    logr_numero = models.CharField(
        db_column='LOGR_NUMERO', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    logr_complemento = models.CharField(
        db_column='LOGR_COMPLEMENTO', max_length=70, blank=True, null=True)
    # Field name made lowercase.
    cep_nota = models.CharField(
        db_column='CEP_NOTA', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=8,
                           blank=True, null=True)
    # Field name made lowercase.
    bairro = models.CharField(
        db_column='BAIRRO', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    cidade = models.CharField(
        db_column='CIDADE', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    latitude_old = models.CharField(db_column='LATITUDE_OLD', max_length=1)
    # Field name made lowercase.
    longitude_old = models.CharField(db_column='LONGITUDE_OLD', max_length=1)
    # Field name made lowercase.
    latitude = models.CharField(
        db_column='LATITUDE', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    longitude = models.CharField(
        db_column='LONGITUDE', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    cadastro_id = models.IntegerField(db_column='CADASTRO_ID')
    # Field name made lowercase.
    dt_inclusao = models.DateField(
        db_column='DT_INCLUSAO', blank=True, null=True)
    # Field name made lowercase.
    deficientecadeirante = models.CharField(
        db_column='DEFICIENTECADEIRANTE', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    deficienteaudio = models.CharField(
        db_column='DEFICIENTEAUDIO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    vintequatrohoras = models.CharField(
        db_column='VINTEQUATROHORAS', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    status = models.CharField(
        db_column='STATUS', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    concessionaria = models.CharField(
        db_column='CONCESSIONARIA', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    dtultimacomunicacao = models.CharField(
        db_column='DTULTIMACOMUNICACAO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    metadado = models.CharField(
        db_column='METADADO', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    sequencia = models.BigIntegerField(
        db_column='SEQUENCIA', blank=True, null=True)
    # Field name made lowercase.
    id_tup = models.CharField(
        db_column='ID_TUP', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    dt_atualizacao = models.DateTimeField(
        db_column='DT_ATUALIZACAO', blank=True, null=True)
    # Field name made lowercase.
    situacao = models.CharField(
        db_column='SITUACAO', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TELEFONES_PUBLICOS'


class TelefonesPublicosOld(models.Model):
    # Field name made lowercase. The composite primary key (DDD, TELEFONE) found, that is not supported. The first column is selected.
    ddd = models.CharField(db_column='DDD', primary_key=True, max_length=2)
    # Field name made lowercase.
    telefone = models.CharField(db_column='TELEFONE', max_length=9)
    # Field name made lowercase.
    dt_ativacao = models.DateTimeField(db_column='DT_ATIVACAO')
    # Field name made lowercase.
    match_end = models.CharField(
        db_column='MATCH_END', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    endereco = models.CharField(
        db_column='ENDERECO', max_length=130, blank=True, null=True)
    # Field name made lowercase.
    logr_tipo = models.CharField(
        db_column='LOGR_TIPO', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    logr_titulo = models.CharField(
        db_column='LOGR_TITULO', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    logr_nome = models.CharField(
        db_column='LOGR_NOME', max_length=60, blank=True, null=True)
    # Field name made lowercase.
    logr_numero = models.CharField(
        db_column='LOGR_NUMERO', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    logr_complemento = models.CharField(
        db_column='LOGR_COMPLEMENTO', max_length=70, blank=True, null=True)
    # Field name made lowercase.
    cep_nota = models.SmallIntegerField(db_column='CEP_NOTA')
    # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=8,
                           blank=True, null=True)
    # Field name made lowercase.
    bairro = models.CharField(
        db_column='BAIRRO', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    cidade = models.CharField(db_column='CIDADE', max_length=50)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2)
    # Field name made lowercase.
    latitude_old = models.CharField(db_column='LATITUDE_OLD', max_length=15)
    # Field name made lowercase.
    longitude_old = models.CharField(db_column='LONGITUDE_OLD', max_length=15)
    # Field name made lowercase.
    latitude = models.FloatField(db_column='LATITUDE', blank=True, null=True)
    # Field name made lowercase.
    longitude = models.FloatField(db_column='LONGITUDE', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TELEFONES_PUBLICOS_OLD'
        unique_together = (('ddd', 'telefone'),)


class TelefoneHistoricoAlteracao(models.Model):
    # Field name made lowercase.
    historico_telefones_id = models.BigIntegerField(
        db_column='HISTORICO_TELEFONES_ID')
    # Field name made lowercase.
    historico_enderecos_id = models.BigIntegerField(
        db_column='HISTORICO_ENDERECOS_ID')
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    ddd = models.CharField(db_column='DDD', max_length=2)
    # Field name made lowercase.
    telefone = models.CharField(db_column='TELEFONE', max_length=9)
    # Field name made lowercase.
    tipo_telefone = models.SmallIntegerField(db_column='TIPO_TELEFONE')
    # Field name made lowercase.
    cadastro_id = models.IntegerField(db_column='CADASTRO_ID')
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)
    # Field name made lowercase.
    dt_atualizacao = models.DateTimeField(
        db_column='DT_ATUALIZACAO', blank=True, null=True)
    # Field name made lowercase.
    fone_nota = models.CharField(
        db_column='FONE_NOTA', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    dt_informacao = models.DateTimeField(
        db_column='DT_INFORMACAO', blank=True, null=True)
    # Field name made lowercase.
    sigilo = models.SmallIntegerField(
        db_column='SIGILO', blank=True, null=True)
    # Field name made lowercase.
    nsu = models.CharField(
        db_column='NSU', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    origem_serasa = models.CharField(
        db_column='ORIGEM_SERASA', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    prioridade = models.IntegerField(
        db_column='PRIORIDADE', blank=True, null=True)
    # Field name made lowercase.
    classificacao = models.CharField(
        db_column='CLASSIFICACAO', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    fonte_name = models.CharField(
        db_column='FONTE_NAME', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    dt_metralhadora = models.DateTimeField(
        db_column='DT_METRALHADORA', blank=True, null=True)
    # Field name made lowercase.
    origem_dado_topdados = models.CharField(
        db_column='ORIGEM_DADO_TOPDADOS', max_length=100)
    # Field name made lowercase.
    id_usuario_consultou = models.IntegerField(
        db_column='ID_USUARIO_CONSULTOU', blank=True, null=True)
    # Field name made lowercase.
    dt_sci_data_consulta = models.DateTimeField(
        db_column='DT_SCI_DATA_CONSULTA', blank=True, null=True)
    # Field name made lowercase.
    dt_alteracao = models.DateTimeField(
        db_column='DT_ALTERACAO', blank=True, null=True)
    # Field name made lowercase.
    id_usuario = models.IntegerField(
        db_column='ID_USUARIO', blank=True, null=True)
    # Field name made lowercase.
    ic_operacao = models.CharField(
        db_column='IC_OPERACAO', max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TELEFONE_HISTORICO_ALTERACAO'


class TelefoneNovos(models.Model):
    # Field name made lowercase.
    telefone_novos_id = models.BigIntegerField(
        db_column='TELEFONE_NOVOS_ID', blank=True, null=True)
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    ddd = models.CharField(
        db_column='DDD', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    telefone = models.CharField(
        db_column='TELEFONE', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    origem_dado_topdados = models.CharField(
        db_column='ORIGEM_DADO_TOPDADOS', max_length=100)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(db_column='DT_INCLUSAO')
    # Field name made lowercase.
    negativado = models.BooleanField(
        db_column='NEGATIVADO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TELEFONE_NOVOS'


class TelefoneNovosBkp(models.Model):
    # Field name made lowercase.
    telefone_novos_id = models.BigIntegerField(
        db_column='TELEFONE_NOVOS_ID', blank=True, null=True)
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    ddd = models.CharField(
        db_column='DDD', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    telefone = models.CharField(
        db_column='TELEFONE', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    origem_dado_topdados = models.CharField(
        db_column='ORIGEM_DADO_TOPDADOS', max_length=100)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(db_column='DT_INCLUSAO')

    class Meta:
        managed = False
        db_table = 'TELEFONE_NOVOS_BKP'


class TelefoneNovosHistoricoAlteracao(models.Model):
    # Field name made lowercase.
    telefone_novos_id = models.BigIntegerField(
        db_column='TELEFONE_NOVOS_ID', blank=True, null=True)
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    ddd = models.CharField(
        db_column='DDD', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    telefone = models.CharField(
        db_column='TELEFONE', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    origem_dado_topdados = models.CharField(
        db_column='ORIGEM_DADO_TOPDADOS', max_length=100)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(db_column='DT_INCLUSAO')
    # Field name made lowercase.
    dt_alteracao = models.DateTimeField(
        db_column='DT_ALTERACAO', blank=True, null=True)
    # Field name made lowercase.
    id_usuario = models.IntegerField(
        db_column='ID_USUARIO', blank=True, null=True)
    # Field name made lowercase.
    ic_operacao = models.CharField(
        db_column='IC_OPERACAO', max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TELEFONE_NOVOS_HISTORICO_ALTERACAO'


class TelefoneQualidade(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', blank=True, null=True)
    # Field name made lowercase.
    ddd = models.CharField(db_column='DDD', max_length=2,
                           blank=True, null=True)
    # Field name made lowercase.
    telefone = models.CharField(
        db_column='TELEFONE', max_length=9, blank=True, null=True)
    # Field name made lowercase.
    qualidade = models.CharField(
        db_column='QUALIDADE', max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TELEFONE_QUALIDADE'


class TempoResidencia(models.Model):
    # Field name made lowercase.
    tempo_residencia_id = models.SmallIntegerField(
        db_column='TEMPO_RESIDENCIA_ID', primary_key=True)
    # Field name made lowercase.
    desc_tempo_residencia = models.CharField(
        db_column='DESC_TEMPO_RESIDENCIA', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TEMPO_RESIDENCIA'


class Tempsistema(models.Model):
    # Field name made lowercase.
    cpfconjuge = models.CharField(
        db_column='CPFCONJUGE', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    contatos_id_conjuge = models.BigIntegerField(
        db_column='CONTATOS_ID_CONJUGE', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TEMPSISTEMA'


class TipoEndereco(models.Model):
    # Field name made lowercase.
    tipo_endereco_id = models.SmallIntegerField(
        db_column='TIPO_ENDERECO_ID', primary_key=True)
    # Field name made lowercase.
    descricao = models.CharField(
        db_column='DESCRICAO', unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'TIPO_ENDERECO'


class TipoFamilia(models.Model):
    # Field name made lowercase.
    tipo_familia_id = models.SmallIntegerField(
        db_column='TIPO_FAMILIA_ID', primary_key=True)
    # Field name made lowercase.
    desc_tipo_familia = models.CharField(
        db_column='DESC_TIPO_FAMILIA', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TIPO_FAMILIA'


class TipoSocio(models.Model):
    # Field name made lowercase.
    tp_socio_id = models.SmallIntegerField(
        db_column='TP_SOCIO_ID', primary_key=True, db_comment='- C¾digo do Tipo de S¾cio')
    # Field name made lowercase.
    tp_socio_descr = models.CharField(
        db_column='TP_SOCIO_DESCR', max_length=20, blank=True, null=True, db_comment='- Nome do Tipo de S¾cio')

    class Meta:
        managed = False
        db_table = 'TIPO_SOCIO'


class TipoTelefone(models.Model):
    # Field name made lowercase.
    tipo_telefone = models.SmallIntegerField(
        db_column='TIPO_TELEFONE', db_comment='- C¾digo do Tipo do Telefone')
    # Field name made lowercase.
    descricao = models.CharField(
        db_column='DESCRICAO', max_length=20, db_comment='- Nome do Tipo do Telefone')

    class Meta:
        managed = False
        db_table = 'TIPO_TELEFONE'


class TmAereoFraudes(models.Model):
    # Field name made lowercase.
    id_chamadotrx = models.BigIntegerField(db_column='ID_CHAMADOTRX')
    # Field name made lowercase.
    merchantreferencenumber = models.CharField(
        db_column='MerchantReferenceNumber', max_length=300, blank=True, null=True)
    frequent_flyer_number = models.CharField(max_length=14)
    # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=100)
    # Field name made lowercase.
    data = models.DateTimeField(db_column='Data', blank=True, null=True)
    # Field name made lowercase.
    tel = models.CharField(
        db_column='Tel', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    obs = models.CharField(
        db_column='Obs', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    analista = models.CharField(
        db_column='Analista', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    tratado = models.CharField(db_column='TRATADO', max_length=1)
    # Field name made lowercase.
    marcacao_cyber = models.CharField(db_column='MARCACAO_CYBER', max_length=1)
    # Field name made lowercase.
    marcacao_tmx = models.CharField(db_column='MARCACAO_TMX', max_length=1)

    class Meta:
        managed = False
        db_table = 'TM_AEREO_FRAUDES'


class TmAereoListaBin(models.Model):
    # Field name made lowercase.
    bin_do_cartao = models.CharField(
        db_column='BIN_DO_CARTAO', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TM_AEREO_LISTA_BIN'


class TmAereoListaFraudes(models.Model):
    # Field name made lowercase.
    cpf_cartao = models.CharField(db_column='CPF_CARTAO', max_length=14)
    # Field name made lowercase.
    desc_nome_cartao = models.CharField(
        db_column='DESC_NOME_CARTAO', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TM_AEREO_LISTA_FRAUDES'


class TmAereoListaVendas(models.Model):
    # Field name made lowercase.
    cpf_cartao = models.CharField(db_column='CPF_CARTAO', max_length=14)
    # Field name made lowercase.
    descricao_vendas = models.CharField(
        db_column='DESCRICAO_VENDAS', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TM_AEREO_LISTA_VENDAS'


class TmAereoStatus(models.Model):
    # Field name made lowercase.
    id_chamadotrx = models.BigIntegerField(db_column='ID_CHAMADOTRX')
    # Field name made lowercase.
    merchantreferencenumber = models.CharField(
        db_column='MerchantReferenceNumber', max_length=300, blank=True, null=True)
    frequent_flyer_number = models.CharField(max_length=14)
    # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=100)
    # Field name made lowercase.
    data = models.DateTimeField(db_column='Data', blank=True, null=True)
    # Field name made lowercase.
    tel = models.CharField(
        db_column='Tel', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    obs = models.CharField(
        db_column='Obs', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    analista = models.CharField(
        db_column='Analista', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TM_AEREO_STATUS'
        primary_key = 'id_chamadotrx'


class TmAereoStatusLog(models.Model):
    # Field name made lowercase.
    id_chamadotrx = models.BigIntegerField(db_column='ID_CHAMADOTRX')
    # Field name made lowercase.
    merchantreferencenumber = models.CharField(
        db_column='MerchantReferenceNumber', max_length=300, blank=True, null=True)
    frequent_flyer_number = models.CharField(max_length=14)
    # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=100)
    # Field name made lowercase.
    data = models.DateTimeField(db_column='Data', blank=True, null=True)
    # Field name made lowercase.
    tel = models.CharField(
        db_column='Tel', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    obs = models.CharField(
        db_column='Obs', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    analista = models.CharField(
        db_column='Analista', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TM_AEREO_STATUS_LOG'


class TmAereoTrx(models.Model):
    # Field name made lowercase.
    merchantid = models.CharField(
        db_column='MerchantID', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    requestid = models.CharField(
        db_column='RequestID', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    transactiondate = models.DateTimeField(
        db_column='TransactionDate', blank=True, null=True)
    # Field name made lowercase.
    merchantreferencenumber = models.CharField(
        db_column='MerchantReferenceNumber', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    billing_firstname = models.CharField(
        db_column='Billing_FirstName', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    billing_lastname = models.CharField(
        db_column='Billing_LastName', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    billing_address1 = models.CharField(
        db_column='Billing_Address1', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    billing_city = models.CharField(
        db_column='Billing_City', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    billing_state = models.CharField(
        db_column='Billing_State', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    billing_postalcode = models.CharField(
        db_column='Billing_PostalCode', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    billing_country = models.CharField(
        db_column='Billing_Country', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    billing_phone = models.CharField(
        db_column='Billing_Phone', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    billing_email = models.CharField(
        db_column='Billing_Email', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    billing_customerid = models.CharField(
        db_column='Billing_CustomerID', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    accountsuffix = models.CharField(
        db_column='AccountSuffix', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    cardbin = models.CharField(
        db_column='CardBIN', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    cardbincountry = models.CharField(
        db_column='CardBINCountry', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    orderamount = models.CharField(
        db_column='OrderAmount', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    ordercurrency = models.CharField(
        db_column='OrderCurrency', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    score = models.CharField(
        db_column='Score', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    factors = models.CharField(
        db_column='Factors', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    infocodestring = models.CharField(
        db_column='InfoCodeString', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    hostseverity = models.CharField(
        db_column='HostSeverity', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    ipaddress = models.CharField(
        db_column='IPAddress', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    iproutingmethod = models.CharField(
        db_column='IPRoutingMethod', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    ipcountry = models.CharField(
        db_column='IPCountry', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    ipstate = models.CharField(
        db_column='IPState', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    ipcity = models.CharField(
        db_column='IPCity', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    completeroute = models.CharField(
        db_column='CompleteRoute', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    departuredatetime = models.DateTimeField(
        db_column='DepartureDateTime', blank=True, null=True)
    # Field name made lowercase.
    active_name = models.CharField(
        db_column='Active_Name', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    active_decision = models.CharField(
        db_column='Active_Decision', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    priority = models.CharField(
        db_column='Priority', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    fingerprint = models.CharField(
        db_column='Fingerprint', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    trueip_address = models.CharField(
        db_column='TrueIP_Address', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    applicationtype = models.CharField(
        db_column='ApplicationType', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    profilingdatetime = models.CharField(
        db_column='ProfilingDateTime', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    profilingduration = models.CharField(
        db_column='ProfilingDuration', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    profiledurl = models.CharField(
        db_column='ProfiledURL', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    timeonpage = models.CharField(
        db_column='TimeOnPage', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    devicematched = models.CharField(
        db_column='DeviceMatched', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    datedevicefirstseen = models.CharField(
        db_column='DateDeviceFirstSeen', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    cpf = models.CharField(
        db_column='CPF', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    titular_do_cartao = models.CharField(
        db_column='Titular_do_cartao', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    horas_para_o_voo = models.CharField(
        db_column='Horas_para_o_voo', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    oac = models.CharField(
        db_column='OAC', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    remarcacao = models.CharField(
        db_column='Remarcacao', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    bin_do_cartao = models.CharField(
        db_column='BIN_do_cartao', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    itinerario_da_remarcacao = models.CharField(
        db_column='Itinerario_da_Remarcacao', max_length=300, blank=True, null=True)
    frequent_flyer_number = models.CharField(max_length=14)
    # Field name made lowercase.
    portal = models.CharField(
        db_column='Portal', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    home = models.CharField(
        db_column='Home', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    mean_of_payment = models.CharField(
        db_column='Mean_of_payment', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    intinerario_por_pais = models.CharField(
        db_column='Intinerario_por_Pais', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    cias_aereas = models.CharField(
        db_column='CIAs_Aereas', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    classes = models.CharField(
        db_column='Classes', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    codigo_e_numero_do_voo = models.CharField(
        db_column='Codigo_e_numero_do_voo', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    nome_passageiro_1 = models.CharField(
        db_column='Nome_Passageiro_1', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    sobrenome_passageiro_1 = models.CharField(
        db_column='Sobrenome_Passageiro_1', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    resgate_de_pontos = models.CharField(
        db_column='Resgate_de_pontos', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    parcelamento = models.CharField(
        db_column='Parcelamento', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    quantidade_de_parcelas = models.CharField(
        db_column='Quantidade_de_parcelas', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    estado_de_emissao_cpf = models.CharField(
        db_column='Estado_de_Emissao_CPF', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    origem_transacao = models.CharField(
        db_column='Origem_Transacao', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    tipo_de_servico = models.CharField(
        db_column='Tipo_de_Servico', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    canal_de_venda = models.CharField(
        db_column='Canal_de_venda', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    detalhes_da_plataforma = models.CharField(
        db_column='Detalhes_da_plataforma', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    qtd_millas_canjeadas = models.CharField(
        db_column='Qtd_millas_canjeadas', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    qtd_millas_disponibles = models.CharField(
        db_column='Qtd_millas_disponibles', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    dinero_compra_millas = models.CharField(
        db_column='Dinero_compra_millas', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    tier_login = models.CharField(
        db_column='Tier_login', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    tag_scoring_latam = models.CharField(
        db_column='TAG_scoring_LATAM', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    footprintid = models.CharField(
        db_column='FootprintID', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    scoring_latam_identity = models.CharField(
        db_column='Scoring_LATAM_Identity', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    orderflow = models.CharField(
        db_column='ORDERFLOW', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    ismigrated = models.CharField(
        db_column='ISMIGRATED', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    medio_de_pago = models.CharField(
        db_column='Medio_de_Pago', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    monto_cc = models.CharField(
        db_column='Monto_CC', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    monto_wallet = models.CharField(
        db_column='Monto_Wallet', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    origem = models.CharField(
        db_column='ORIGEM', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)
    id = models.BigAutoField(db_column='ID')  # Field name made lowercase.
    # Field name made lowercase.
    analista = models.CharField(
        db_column='Analista', max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TM_AEREO_TRX'


class TmListaLubber(models.Model):
    ffp_num = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    pnr_code = models.CharField(max_length=50, blank=True, null=True)
    passenger_name = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TM_LISTA_LUBBER'


class TmNaoAereo(models.Model):
    # Field name made lowercase.
    id = models.BigAutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    login = models.CharField(
        db_column='Login', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    numero_pedido = models.BigIntegerField(db_column='Numero_Pedido')
    # Field name made lowercase.
    nome_usuario = models.CharField(
        db_column='Nome_usuario', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    data_da_compra = models.DateField(db_column='Data_da_compra')
    # Field name made lowercase.
    hora_da_compra = models.TimeField(
        db_column='Hora_da_compra', blank=True, null=True)
    # Field name made lowercase.
    fornecedor = models.CharField(
        db_column='Fornecedor', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    item = models.CharField(
        db_column='Item', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    status_pedido = models.CharField(
        db_column='Status_pedido', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    tipo_produto = models.CharField(
        db_column='Tipo_Produto', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    logradouro = models.CharField(
        db_column='Logradouro', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    bairro = models.CharField(
        db_column='Bairro', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    cidade = models.CharField(
        db_column='Cidade', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=4, blank=True, null=True)
    # Field name made lowercase.
    cep = models.CharField(
        db_column='CEP', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    telefone = models.CharField(
        db_column='Telefone', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    email_pedido = models.CharField(
        db_column='Email_pedido', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    valor_item_pago_pontos = models.IntegerField(
        db_column='Valor_item_pago_pontos', blank=True, null=True)
    # Field name made lowercase.
    origem = models.CharField(
        db_column='ORIGEM', max_length=500, blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TM_NAO_AEREO'


class TbIrpf(models.Model):
    # Field name made lowercase.
    docnumber = models.CharField(
        db_column='DocNumber', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    instituicao_bancaria = models.CharField(
        db_column='Instituicao_Bancaria', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    cod_agencia = models.CharField(
        db_column='Cod_Agencia', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    lote = models.CharField(
        db_column='Lote', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    ano_referencia = models.CharField(
        db_column='Ano_Referencia', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    dt_lote = models.DateTimeField(db_column='Dt_Lote', blank=True, null=True)
    # Field name made lowercase.
    sit_receita_federal = models.CharField(
        db_column='Sit_Receita_Federal', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    dt_consulta = models.DateTimeField(
        db_column='Dt_Consulta', blank=True, null=True)
    # Field name made lowercase.
    cadastro_id = models.IntegerField(db_column='CADASTRO_ID')
    # Field name made lowercase.
    cpf = models.CharField(
        db_column='CPF', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(db_column='DT_INCLUSAO')

    class Meta:
        managed = False
        db_table = 'Tb_IRPF'


class TesteLuccas(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    cpf = models.CharField(
        db_column='CPF', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    nome = models.CharField(
        db_column='NOME', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    nasc = models.DateTimeField(db_column='NASC', blank=True, null=True)
    # Field name made lowercase.
    rg = models.CharField(db_column='RG', max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Teste_Luccas'


class Uiproperties(models.Model):
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UIProperties'


class Usuario(models.Model):
    # Field name made lowercase.
    id_usuario = models.IntegerField(db_column='ID_USUARIO')
    # Field name made lowercase.
    ds_nome = models.CharField(db_column='DS_NOME', max_length=100)
    # Field name made lowercase.
    ds_usuario = models.CharField(db_column='DS_USUARIO', max_length=100)
    # Field name made lowercase.
    ds_senha = models.CharField(db_column='DS_SENHA', max_length=1000)
    # Field name made lowercase.
    ic_ativo = models.CharField(db_column='IC_ATIVO', max_length=1)
    # Field name made lowercase.
    nu_cpf = models.CharField(
        db_column='NU_CPF', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)
    # Field name made lowercase.
    id_perfil = models.SmallIntegerField(
        db_column='ID_PERFIL', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'USUARIO'


class UsuarioLog(models.Model):
    # Field name made lowercase.
    id_usuario = models.IntegerField(db_column='ID_USUARIO')
    # Field name made lowercase.
    dt_atividade = models.DateTimeField(db_column='DT_ATIVIDADE')
    # Field name made lowercase.
    ds_atividade = models.CharField(db_column='DS_ATIVIDADE', max_length=30)
    # Field name made lowercase.
    nu_cpf = models.CharField(
        db_column='NU_CPF', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    ds_usuario = models.CharField(
        db_column='DS_USUARIO', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    nu_telefone = models.CharField(
        db_column='NU_TELEFONE', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    ds_email = models.CharField(
        db_column='DS_EMAIL', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', blank=True, null=True)
    # Field name made lowercase.
    ds_endereco = models.CharField(
        db_column='DS_ENDERECO', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    nu_cnpj = models.CharField(
        db_column='NU_CNPJ', max_length=14, blank=True, null=True)
    # Field name made lowercase.
    ds_telefone = models.CharField(
        db_column='DS_TELEFONE', max_length=15, blank=True, null=True)
    # Field name made lowercase.
    ds_email_edit = models.CharField(
        db_column='DS_EMAIL_EDIT', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'USUARIO_LOG'


class VeiculosEmpresas(models.Model):
    # Field name made lowercase.
    veiculos_empresas_id = models.BigIntegerField(
        db_column='VEICULOS_EMPRESAS_ID', blank=True, null=True)
    # Field name made lowercase.
    cnpj = models.CharField(
        db_column='CNPJ', max_length=14, blank=True, null=True)
    # Field name made lowercase.
    placa = models.CharField(
        db_column='PLACA', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    marca = models.CharField(
        db_column='MARCA', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    renavan = models.CharField(
        db_column='RENAVAN', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    anofab = models.CharField(
        db_column='ANOFAB', max_length=8, blank=True, null=True)
    # Field name made lowercase.
    chassi = models.CharField(
        db_column='CHASSI', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    anomode = models.CharField(
        db_column='ANOMODE', max_length=8, blank=True, null=True)
    # Field name made lowercase.
    propri = models.CharField(
        db_column='PROPRI', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    endereco = models.CharField(
        db_column='ENDERECO', max_length=903, blank=True, null=True)
    # Field name made lowercase.
    bairro = models.CharField(
        db_column='BAIRRO', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    cep = models.CharField(
        db_column='CEP', max_length=16, blank=True, null=True)
    # Field name made lowercase.
    cidade = models.CharField(
        db_column='CIDADE', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    estado = models.CharField(
        db_column='ESTADO', max_length=4, blank=True, null=True)
    # Field name made lowercase.
    origem = models.CharField(
        db_column='ORIGEM', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    dt_atualizacao = models.DateTimeField(
        db_column='DT_ATUALIZACAO', blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VEICULOS_EMPRESAS'


class VeiculoPessoaFisica(models.Model):
    # Field name made lowercase.
    veiculo_id = models.BigIntegerField(
        db_column='VEICULO_ID', primary_key=True)
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    cpf = models.CharField(
        db_column='CPF', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    placa = models.CharField(
        db_column='PLACA', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    marca = models.CharField(
        db_column='MARCA', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    renavan = models.CharField(
        db_column='RENAVAN', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    anofab = models.CharField(
        db_column='ANOFAB', max_length=8, blank=True, null=True)
    # Field name made lowercase.
    chassi = models.CharField(
        db_column='CHASSI', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    anomode = models.CharField(
        db_column='ANOMODE', max_length=8, blank=True, null=True)
    # Field name made lowercase.
    propri = models.CharField(
        db_column='PROPRI', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    end = models.CharField(
        db_column='END', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    num = models.CharField(
        db_column='NUM', max_length=10, blank=True, null=True)
    # Field name made lowercase.
    compl = models.CharField(
        db_column='COMPL', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    bairro = models.CharField(
        db_column='BAIRRO', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    cep = models.CharField(
        db_column='CEP', max_length=16, blank=True, null=True)
    # Field name made lowercase.
    cidade = models.CharField(
        db_column='CIDADE', max_length=300, blank=True, null=True)
    # Field name made lowercase.
    estado = models.CharField(
        db_column='ESTADO', max_length=4, blank=True, null=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(db_column='DT_INCLUSAO')
    # Field name made lowercase.
    dt_atualizacao = models.DateTimeField(
        db_column='DT_ATUALIZACAO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VEICULO_PESSOA_FISICA'


class VivoEmpresas(models.Model):
    # Field name made lowercase.
    cnpj = models.CharField(
        db_column='CNPJ', max_length=14, blank=True, null=True)
    # Field name made lowercase.
    qtd_telefones = models.IntegerField(
        db_column='QTD_TELEFONES', blank=True, null=True)
    # Field name made lowercase.
    valor = models.IntegerField(db_column='VALOR', blank=True, null=True)
    # Field name made lowercase.
    flg_cliente = models.IntegerField(
        db_column='FLG_CLIENTE', blank=True, null=True)
    # Field name made lowercase.
    flg_descanso = models.IntegerField(
        db_column='FLG_DESCANSO', blank=True, null=True)
    # Field name made lowercase.
    carteira = models.CharField(
        db_column='CARTEIRA', max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VIVO_EMPRESAS'


class VivoEmpresasSocios(models.Model):
    # Field name made lowercase.
    cnpj = models.CharField(
        db_column='CNPJ', max_length=14, blank=True, null=True)
    # Field name made lowercase.
    tp_doc_socio = models.CharField(
        db_column='TP_DOC_SOCIO', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    nr_doc_socio = models.CharField(
        db_column='NR_DOC_SOCIO', max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VIVO_EMPRESAS_SOCIOS'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class Sysschemaarticles(models.Model):
    artid = models.IntegerField()
    creation_script = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    dest_object = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    objid = models.IntegerField()
    pubid = models.IntegerField()
    pre_creation_cmd = models.SmallIntegerField()
    status = models.IntegerField()
    type = models.SmallIntegerField()
    # This field type is a guess.
    schema_option = models.TextField(blank=True, null=True)
    dest_owner = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysschemaarticles'
        unique_together = (('artid', 'pubid'),)


class Tempfinaltabela(models.Model):
    # Field name made lowercase.
    cpf = models.CharField(
        db_column='CPF', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', blank=True, null=True)
    # Field name made lowercase.
    nome = models.CharField(
        db_column='NOME', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    nasc = models.DateTimeField(db_column='NASC', blank=True, null=True)
    # Field name made lowercase.
    sexo = models.CharField(
        db_column='SEXO', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    nome_mae = models.CharField(
        db_column='NOME_MAE', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    email = models.CharField(
        db_column='EMAIL', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tempfinaltabela'


class Tempfinaltabelaendereco(models.Model):
    # Field name made lowercase.
    cpf = models.CharField(
        db_column='CPF', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    nome = models.CharField(
        db_column='NOME', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(db_column='CONTATOS_ID')
    # Field name made lowercase.
    endereco = models.CharField(
        db_column='ENDERECO', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    bairro = models.CharField(
        db_column='BAIRRO', max_length=40, blank=True, null=True)
    # Field name made lowercase.
    cidade = models.CharField(
        db_column='CIDADE', max_length=40, blank=True, null=True)
    # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)
    # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=8,
                           blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tempfinaltabelaendereco'


class Temptelefonefinal(models.Model):
    # Field name made lowercase.
    cpf = models.CharField(
        db_column='CPF', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    nome = models.CharField(
        db_column='NOME', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    telefone1 = models.CharField(
        db_column='TELEFONE1', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    telefone2 = models.CharField(
        db_column='TELEFONE2', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    telefone3 = models.CharField(
        db_column='TELEFONE3', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    telefone4 = models.CharField(
        db_column='TELEFONE4', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    telefone5 = models.CharField(
        db_column='TELEFONE5', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    telefone6 = models.CharField(
        db_column='TELEFONE6', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    telefone7 = models.CharField(
        db_column='TELEFONE7', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    telefone8 = models.CharField(
        db_column='TELEFONE8', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    telefone9 = models.CharField(
        db_column='TELEFONE9', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    telefone10 = models.CharField(
        db_column='TELEFONE10', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    telefone11 = models.CharField(
        db_column='TELEFONE11', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    telefone12 = models.CharField(
        db_column='TELEFONE12', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    telefone13 = models.CharField(
        db_column='TELEFONE13', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    telefone14 = models.CharField(
        db_column='TELEFONE14', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    telefone15 = models.CharField(
        db_column='TELEFONE15', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    telefone16 = models.CharField(
        db_column='TELEFONE16', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    telefone17 = models.CharField(
        db_column='TELEFONE17', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    telefone18 = models.CharField(
        db_column='TELEFONE18', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    telefone19 = models.CharField(
        db_column='TELEFONE19', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    telefone20 = models.CharField(
        db_column='TELEFONE20', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    telefone21 = models.CharField(
        db_column='TELEFONE21', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    telefone22 = models.CharField(
        db_column='TELEFONE22', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    telefone23 = models.CharField(
        db_column='TELEFONE23', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    telefone24 = models.CharField(
        db_column='TELEFONE24', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    telefone25 = models.CharField(
        db_column='TELEFONE25', max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temptelefonefinal'
