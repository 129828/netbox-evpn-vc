import strawberry
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
    @strawberry.field
    def evpn_vcs(self) -> list[EvpnVCType]:
        return models.EvpnVC.objects.all()

    @strawberry.field
    def evpn_vc_vlans(self) -> list[EvpnVCVlanType]:
        return models.EvpnVCVlan.objects.all()

    @strawberry.field
    def evpn_vc_types(self) -> list[EvpnVCTypeType]:
        return models.EvpnVCType.objects.all()