from api.models import RowPermitData
from api.serializers import RowPermitDataSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class RowPermitDataViewSet(viewsets.ModelViewSet):
    
    queryset = RowPermitData.objects.all()
    serializer_class = RowPermitDataSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter,)
    search_fields = ('permit_id',  'district', 'permit_category', 'type',
                     'district', 'name', 'mailing_address', 'city_state',
                     'location', 'cross_street', 'street_number', 'direction',
                     'street', 'street_type', 'city', 'state', 'zip_code',
                     'check_no', 'orsp', 'agent_address')
    filter_fields = ('city_state', 'entry_date', 'issue_date',
                     'expiration_date', 'final_date', 'effect_date', 'fee',
                     'receipts', 'lat_lng', 'geo_coded', 'deposit_amount',
                     'deposit_received', 'deposit_returned', 'insurance',
                     'lat_from_lat_lng', 'long_from_lat_lng', 'lat_from_orsp',
                     'long_from_orsp'
                     )
    ordering_fields = '__all__'
