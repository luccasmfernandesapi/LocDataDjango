from django.db import models
from consultacpf.models import PessoaFisica


class TmAereoTrx(models.Model):
    # Field name made lowercase.
    id = models.BigAutoField(db_column='ID', primary_key=True)
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

    frequent_flyer_number = models.ForeignKey(
        PessoaFisica, on_delete=models.PROTECT, max_length=14, related_name="dados_pessoal", to_field='cpf', db_column="frequent_flyer_number")

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

    # Field name made lowercase.
    analista = models.CharField(
        db_column='Analista', max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TM_AEREO_TRX'


class TmAereoStatus(models.Model):
    # Field name made lowercase.
    id_chamadotrx = models.OneToOneField(TmAereoTrx, on_delete=models.CASCADE,
                                         related_name="status_transacao", db_column="ID_CHAMADOTRX", primary_key=True)
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
