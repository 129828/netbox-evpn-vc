import django_filters
from django.db.models import Q
from ipam.models import VLAN
from netbox.filtersets import NetBoxModelFilterSet
from tenancy.models import Tenant
from virtualization.models import Cluster

from .models import EvpnVC, EvpnVCType, EvpnVCVlan


class EvpnVCTypeFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = EvpnVCType
        fields = ('id', 'name', 'description')

    def search(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value))


class EvpnVCFilterSet(NetBoxModelFilterSet):
    tenant_id = django_filters.ModelMultipleChoiceFilter(
        field_name='tenant__id',
        queryset=Tenant.objects.all(),
        to_field_name='id',
        label='Tenant (ID)',
    )
    clusters = django_filters.ModelMultipleChoiceFilter(
        field_name='clusters__id',
        queryset=Cluster.objects.all(),
        to_field_name='id',
        label='Clusters (ID)',
    )

    class Meta:
        model = EvpnVC
        fields = ('id', 'name', 'vni', 'vc_type', 'tenant', 'clusters')

    def search(self, queryset, name, value):
        qs_filter = (
            Q(id__icontains=value)
            | Q(name__icontains=value)
            | Q(vni__icontains=value)
            | Q(clusters__name__icontains=value)
        )
        # the clusters join can return the same VC multiple times
        return queryset.filter(qs_filter).distinct()


class EvpnVCVlanFilterSet(NetBoxModelFilterSet):
    evpn_vc_id = django_filters.ModelMultipleChoiceFilter(
        field_name='evpn_vc__id',
        queryset=EvpnVC.objects.all(),
        to_field_name='id',
        label='EVPN VC (ID)',
    )
    vlan_id = django_filters.ModelMultipleChoiceFilter(
        field_name='vlan__id',
        queryset=VLAN.objects.all(),
        to_field_name='id',
        label='VLAN (ID)',
    )

    class Meta:
        model = EvpnVCVlan
        fields = ('id', 'evpn_vc', 'vlan')

    def search(self, queryset, name, value):
        qs_filter = (
            Q(id__icontains=value)
            | Q(vlan__name__icontains=value)
            | Q(evpn_vc__name__icontains=value)
        )
        return queryset.filter(qs_filter)
