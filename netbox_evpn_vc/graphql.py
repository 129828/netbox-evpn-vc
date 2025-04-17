import strawberry
import strawberry_django
from typing import Optional, Annotated, List
from . import models


@strawberry_django.type(models.EvpnVC, fields="__all__")
class EvpnVCType:
    pass


@strawberry_django.type(models.EvpnVCVlan, fields="__all__")
class EvpnVCVlanType:
    evpn_vc: Optional[EvpnVCType]
    evpnvcvlan: Annotated["vlan", strawberry.lazy("ipam.graphql.types")]


@strawberry_django.type(models.EvpnVCType, fields="__all__")
class EvpnVCTypeType:
    pass


@strawberry.type
class Query:
    @strawberry.field
    def evpn_vcs(self, id: int) -> EvpnVCType:
        return None
    evpn_vcs_list: list[EvpnVCType] = strawberry_django.field()

    @strawberry.field
    def evpn_vc_vlans(self, id: int) -> EvpnVCVlanType:
        return models.EvpnVCVlan.objects.filter(id=id).first()

    evpn_vc_vlans_list: list[EvpnVCVlanType] = strawberry_django.field()

    @strawberry.field
    def evpn_vc_types(self, id: int) -> EvpnVCTypeType:
        return None
    evpn_vc_types_list: list[EvpnVCTypeType] = strawberry_django.field()


schema = [
    Query,
]