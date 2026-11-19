from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from netbox.plugins import PluginTemplateExtension

from . import tables


class EvpnVCVLANStatus(PluginTemplateExtension):
    models = ["ipam.vlan"]

    def right_page(self):
        vlan = self.context["object"]

        try:
            evpnvcvlan = vlan.evpnvcvlan
        except ObjectDoesNotExist:
            return ""

        return self.render(
            "netbox_evpn_vc/vlan_evpn_vc.html",
            extra_context={"evpnvcvlan": evpnvcvlan},
        )


class TenantEvpnVCs(PluginTemplateExtension):
    models = ["tenancy.tenant"]

    def right_page(self):
        tenant = self.context["object"]
        vcs = tables.EvpnVCTenantTable(
            tenant.evpnvcs.annotate(vlan_count=Count('vlans')),
            orderable=False,
        )

        return self.render(
            "netbox_evpn_vc/tenant_evpn_vc.html",
            extra_context={"evpnvcs": vcs},
        )


template_extensions = [EvpnVCVLANStatus, TenantEvpnVCs]
