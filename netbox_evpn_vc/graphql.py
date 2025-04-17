import strawberry
from netbox.graphql.query import ObjectQuery
from strawberry_django.type import type as django_type
from . import models, filtersets

@django_type(models.EvpnVC)
class EvpnVCType:
    pass

@django_type(models.EvpnVCVlan, filters=filtersets.EvpnVCVlanFilterSet)
class EvpnVCVlanType:
    pass

@django_type(models.EvpnVCType)
class EvpnVCTypeType:
    pass

@strawberry.type
class Query:
    evpn_vc: ObjectQuery[EvpnVCType] = ObjectQuery(model=models.EvpnVC)
    evpn_vc_vlan: ObjectQuery[EvpnVCVlanType] = ObjectQuery(model=models.EvpnVCVlan, filterset_class=filtersets.EvpnVCVlanFilterSet)
    evpn_vc_type: ObjectQuery[EvpnVCTypeType] = ObjectQuery(model=models.EvpnVCType)