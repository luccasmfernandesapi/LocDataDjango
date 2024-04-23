from django.db import models
from datetime import datetime


class Ocupacao(models.Model):
    # Field name made lowercase.
    cbo = models.IntegerField(db_column='CBO', primary_key=True)
    titulo = models.CharField(max_length=255)
    # Field name made lowercase.
    codfamilia = models.SmallIntegerField(db_column='CodFamilia')
    # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=8)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"
        managed = False
        db_table = '[Produtivo].[OCUPACAO]'


class PessoaFisica(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', primary_key=True, blank=True)
    # Field name made lowercase.
    cpf = models.CharField(
        db_column='CPF', max_length=11, blank=False, null=False, unique=True)
    # Field name made lowercase.
    nome = models.CharField(
        db_column='NOME', max_length=100, blank=False, null=False)
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
    sexo = models.CharField(
        db_column='SEXO', max_length=1, blank=True, null=True)
    # Field name made lowercase.
    nasc = models.DateTimeField(db_column='NASC', blank=False, null=False)
    # Field name made lowercase.
    nome_civil = models.CharField(
        db_column='NOME_CIVIL', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    nome_mae = models.CharField(
        db_column='NOME_MAE', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    nome_pai = models.CharField(
        db_column='NOME_PAI', max_length=100, blank=True, null=True)

    estado_civil = {
        "C":	"CASADO",
        "S":	"SOLTEIRO",
        "D":	"DIVORCIADO",
        "V":	"VIUVO",
        "O":	"OUTROS",
        None: ""
    }

    estciv = models.CharField(
        db_column='ESTCIV', max_length=1, blank=True, null=True, choices=estado_civil)
    # Field name made lowercase.
    rg = models.CharField(db_column='RG', max_length=30, blank=True, null=True)
    # Field name made lowercase.
    situacaocadastral = {
        1: "INFORMACAO NAO EXISTENTE NA RECEITA",
        2: "REGULAR",
        3: "PENDENTE DE REGULARIZACAO",
        4:	"NULA",
        6:	"SUSPENSA",
        9:	"CANCELADA",
        10:	"TITULAR FALECIDO",
    }
    cd_sit_cad = models.SmallIntegerField(
        db_column='CD_SIT_CAD', blank=True, null=True, choices=situacaocadastral)
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
    sexo_retratado = models.CharField(
        db_column='SEXO_RETRATADO', max_length=1, blank=True, null=True)
    cbo = models.ForeignKey(
        Ocupacao, on_delete=models.PROTECT, db_column='cbo')
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
    dt_ob = models.DateTimeField(
        db_column='DT_OB', blank=True, null=True, verbose_name="Data Obito")
    # Field name made lowercase.
    renda = models.DecimalField(
        db_column='RENDA', max_digits=8, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    titulo_eleitor = models.CharField(
        db_column='TITULO_ELEITOR', max_length=20, blank=True, null=True)
    # Field name made lowercase.
    origem_dado_topdados = models.CharField(
        db_column='ORIGEM_DADO_TOPDADOS', max_length=100, default="Cadastro Django", blank=False, null=False)
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

    def save(self, *args, **kwargs):
        if not self.contatos_id:
            self.contatos_id = get_next_contatos_id()
        super(PessoaFisica, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Pessoa Fisica"
        verbose_name_plural = "Pessoa Fisica"
        managed = False
        db_table = "[Produtivo].[PESSOA_FISICA]"

    def __str__(self):
        return f"{self.cpf} - {self.nome} -  {self.nasc}"


class Email(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', blank=True, null=False)
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
        db_column='CADASTRO_ID', max_length=255, blank=True, null=False, primary_key=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EMAIL'


class EmailNovos(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', blank=True, null=False)
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
        db_column='CADASTRO_ID', max_length=255, blank=True, null=False, primary_key=True)
    # Field name made lowercase.
    dt_inclusao = models.DateTimeField(
        db_column='DT_INCLUSAO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = '[Produtivo].[EMAIL]'


class Naturalidade(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', primary_key=True)
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


class TbEscolaridade(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', unique=True, blank=True, null=False, primary_key=True)
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


class TbCns(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', primary_key=True)
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


class TbPis(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', primary_key=True)
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


class TbNis(models.Model):
    # Field name made lowercase.
    contatos_id = models.IntegerField(
        db_column='CONTATOS_ID', primary_key=True)
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


class TbCtps(models.Model):
    # Field name made lowercase.
    ctps_id = models.BigIntegerField(
        db_column='CTPS_ID', unique=True, blank=True, null=False, primary_key=True)
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


class Relacionamento(models.Model):
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', primary_key=True)
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
        db_table = '[Produtivo].[RELACIONAMENTO]'


class Endereco(models.Model):
    # Field name made lowercase.
    historico_enderecos_id = models.BigIntegerField(
        db_column='HISTORICO_ENDERECOS_ID')
    # Field name made lowercase.
    contatos_id = models.OneToOneField(PessoaFisica, related_name='enderecos',
                                       db_column='CONTATOS_ID', primary_key=True, on_delete=models.PROTECT, to_field='contatos_id')
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
        db_table = '[Produtivo].[ENDERECO]'


class EnderecoNovos(models.Model):
    # Field name made lowercase.
    endereco_novos_id = models.BigIntegerField(
        db_column='ENDERECO_NOVOS_ID', blank=True, null=True)
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', primary_key=True)
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
        db_table = '[Produtivo].[ENDERECO_NOVOS]'


class Empresas(models.Model):
    # Field name made lowercase.
    empresas_id = models.IntegerField(
        db_column='EMPRESAS_ID', primary_key=True)
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
        db_table = '[Produtivo].[EMPRESAS]'


class EmpresasSocios(models.Model):
    # Field name made lowercase.
    empresas_id = models.IntegerField(
        db_column='EMPRESAS_ID', blank=True, null=False, primary_key=True)
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
        db_table = '[Produtivo].[EMPRESAS_SOCIOS]'


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
        db_table = '[Produtivo].[MPRESAS_CNAE]'


class Telefone(models.Model):
    # Field name made lowercase.
    historico_telefones_id = models.BigIntegerField(
        db_column='HISTORICO_TELEFONES_ID')
    # Field name made lowercase.
    historico_enderecos_id = models.BigIntegerField(
        db_column='HISTORICO_ENDERECOS_ID')
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', primary_key=True)
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
        db_table = '[Produtivo].[TELEFONE]'


class TelefoneNovos(models.Model):
    # Field name made lowercase.
    telefone_novos_id = models.BigIntegerField(
        db_column='TELEFONE_NOVOS_ID', blank=True, null=True)
    # Field name made lowercase.
    contatos_id = models.BigIntegerField(
        db_column='CONTATOS_ID', primary_key=True)
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
        db_table = '[Produtivo].[TELEFONE_NOVOS]'


class TbEmpregos(models.Model):
    # Field name made lowercase.
    empregos_id = models.BigIntegerField(
        db_column='EMPREGOS_ID', unique=True, blank=True, null=False, primary_key=True)
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


def get_next_contatos_id():
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT MAX(CONTATOS_ID) FROM TopDados.Produtivo.PESSOA_FISICA")
        row = cursor.fetchone()
        max_id = row[0] if row[0] is not None else 0
    return max_id + 1
