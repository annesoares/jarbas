from datetime import datetime, timezone

from django.db import models
from django.utils.timezone import get_default_timezone

UNIX_EPOCH = default=datetime(1970, 1, 1, 0, 0, 0, tzinfo=timezone.utc)


class Document(models.Model):

    document_id = models.IntegerField('Document ID', db_index=True)
    congressperson_name = models.CharField('Congressperson name', max_length=128)
    congressperson_id = models.IntegerField('Congressperson ID', db_index=True)
    congressperson_document = models.IntegerField('Congressperson document')
    term = models.IntegerField('Term', db_index=True)
    state = models.CharField('State', max_length=2)
    party = models.CharField('Party', db_index=True, max_length=16)
    term_id = models.IntegerField('Term ID')
    subquota_number = models.IntegerField('Subquote ID', db_index=True)
    subquota_description = models.CharField('Subquota descrition', max_length=128)
    subquota_group_id = models.IntegerField('Subquota group ID', db_index=True)
    subquota_group_description = models.CharField('Subquota group description', max_length=128)
    supplier = models.CharField('Supplier', max_length=128)
    cnpj_cpf = models.CharField('CNPJ or CPF', db_index=True, max_length=14)
    document_number = models.CharField('Document number', max_length=128)
    document_type = models.IntegerField('Document type', db_index=True)
    issue_date = models.DateTimeField('Issue date', blank=True, null=True)
    document_value = models.DecimalField('Document value', max_digits=10, decimal_places=3)
    remark_value = models.DecimalField('Remark value', max_digits=10, decimal_places=3)
    net_value = models.DecimalField('Net value', max_digits=10, decimal_places=3)
    month = models.IntegerField('Month', db_index=True)
    year = models.IntegerField('Year', db_index=True)
    installment = models.IntegerField('Installment')
    passenger = models.CharField('Passenger', max_length=128)
    leg_of_the_trip = models.CharField('Leg of the trip', max_length=128)
    batch_number = models.IntegerField('Batch number')
    reimbursement_number = models.IntegerField('Reimbursement number', db_index=True)
    reimbursement_value = models.DecimalField('Reimbusrsement value', max_digits=10, decimal_places=3)
    applicant_id = models.IntegerField('Applicant ID', db_index=True)
    source = models.CharField('CSV file source', db_index=True, null=True, blank=True, max_length=16)
    line = models.IntegerField('Line # in the source', db_index=True, null=True, blank=True)
    receipt_url = models.URLField('Receipt URL', null=True, blank=True, default=None, max_length=16)
    receipt_url_last_update = models.URLField('Receipt URL Last Update', db_index=True, default=UNIX_EPOCH)

    def get_receipt_url(self):
        server = 'www.camara.gov.br'
        path = 'cota-parlamentar/documentos/publ/{}/{}/{}.pdf'.format(
            self.applicant_id,
            self.year,
            self.document_id
        )
        return 'http://{}/{}'.format(server, path)
