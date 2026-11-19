import django_tables2 as tables

from netbox.tables import NetBoxTable
from .models import EvpnVC, EvpnVCVlan, EvpnVCType


class EvpnVCTypeTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = EvpnVCType
        fields = ('pk', 'name', 'description')
        default_columns = ('name', 'description')


class EvpnVCTable(NetBoxTable):
    vni = tables.Column(
        linkify=True
    )
    vc_type = tables.Column(
        linkify=True
    )
    tenant = tables.Column(
        linkify=True
    )
    vlan_count = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = EvpnVC
        fields = ('pk', 'vni', 'name', 'vc_type', 'comments', 'tenant', 'clusters', 'vlan_count')
        default_columns = ('vni', 'name', 'vc_type', 'tenant', 'clusters', 'vlan_count')


class EvpnVCTenantTable(NetBoxTable):
    vni = tables.Column(
        linkify=True
    )
    vlan_count = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = EvpnVC
        fields = ('pk', 'vni', 'name', 'comments', 'tenant', 'vlan_count')
        default_columns = ('vni', 'name', 'vlan_count')


class EvpnVCVlanTable(NetBoxTable):
    vlan = tables.Column(
        linkify=True
    )
    evpn_vc = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = EvpnVCVlan
        fields = ('pk', 'evpn_vc', 'vlan')
        default_columns = ('pk', 'vlan')


class EvpnVCVlanListTable(EvpnVCVlanTable):
    class Meta(EvpnVCVlanTable.Meta):
        default_columns = ('pk', 'evpn_vc', 'vlan')
