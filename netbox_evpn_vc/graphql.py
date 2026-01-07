import strawberry
import strawberry_django

# from netbox.graphql.filter_mixins import autotype_decorator, BaseFilterMixin
from netbox.graphql.filter_mixins import BaseFilter
from typing import Optional, Annotated, List
from netbox.graphql.types import NetBoxObjectType
from . import models

from .filtersets import (
    EvpnVCVlanFilterSet
)


@strawberry_django.type(models.EvpnVC, fields="__all__")
class EvpnVCType(NetBoxObjectType):
    pass


@strawberry_django.filter(models.EvpnVCVlan, lookups=True)
# @autotype_decorator(EvpnVCVlanFilterSet)
class EvpnVCVlanFilter(BaseFilter):
    vlan_id: Optional[List[strawberry.ID]]
    evpn_vc_id: Optional[List[strawberry.ID]]


@strawberry_django.type(models.EvpnVCVlan, fields="__all__", filters=EvpnVCVlanFilter)
class EvpnVCVlanType(NetBoxObjectType):
    evpn_vc: Optional[EvpnVCType]
    vlan: Annotated["VLANType", strawberry.lazy("ipam.graphql.types")]


@strawberry_django.type(models.EvpnVCType, fields="__all__")
class EvpnVCTypeType(NetBoxObjectType):
    pass


@strawberry.type(name="Query")
class EVPNQuery:

    evpn_vcs: EvpnVCType = strawberry_django.field()
    evpn_vcs_list: list[EvpnVCType] = strawberry_django.field()

    evpn_vc_vlans: EvpnVCVlanType = strawberry_django.field()
    evpn_vc_vlans_list: list[EvpnVCVlanType] = strawberry_django.field()

    evpn_vc_types: EvpnVCTypeType = strawberry_django.field()
    evpn_vc_types_list: list[EvpnVCTypeType] = strawberry_django.field()


schema = [
    EVPNQuery,
]