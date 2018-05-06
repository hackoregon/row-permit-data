from django.db import models


class RowPermitData(models.Model):
    """
    Model for the `row_permit_data`
    """
    permit_id = models.IntegerField(primary_key=True)
    entry_date = models.DurationField(blank=True, null=True)
    issue_date = models.DurationField(blank=True, null=True)
    permit_category = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    district = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    mailing_address = models.TextField(blank=True, null=True)
    city_state = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    cross_street = models.TextField(blank=True, null=True)
    street_number = models.IntegerField(blank=True, null=True)
    direction = models.TextField(blank=True, null=True)
    street = models.TextField(blank=True, null=True)
    street_type = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    expiration_date = models.DurationField(blank=True, null=True)
    final_date = models.DurationField(blank=True, null=True)
    effect_date = models.DurationField(blank=True, null=True)
    fee = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    receipts = models.TextField(blank=True, null=True)
    check_no = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    lat_lng = models.TextField(blank=True, null=True)
    orsp = models.TextField(blank=True, null=True)
    geo_coded = models.NullBooleanField()
    deposit_amount = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    deposit_received = models.DurationField(blank=True, null=True)
    deposit_returned = models.DurationField(blank=True, null=True)
    insurance = models.NullBooleanField()
    agent_address = models.TextField(blank=True, null=True)
    lat_from_lat_lng = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=7)
    long_from_lat_lng = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=7)
    lat_from_orsp = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=7)
    long_from_orsp = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=7)

    class Meta:
        managed = False
        db_table = 'row_permit_data'
