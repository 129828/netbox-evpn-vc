from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from django.db.models import Count
from netbox.plugins import PluginTemplateExtension
from . import tables

class EvpnVCVLANStatus(PluginTemplateExtension):
    model = "ipam.vlan"
    def right_page(self):
        vlan = self.context["object"]
        template_filename = "netbox_evpn_vc/vlan_evpn_vc.html"

        try:
            return self.render(
                template_filename, extra_context={"evpnvcvlan": vlan.evpnvcvlan}
            )
        except ObjectDoesNotExist:
            return ""

class TenantEvpnVCs(PluginTemplateExtension):
    model = "tenancy.tenant"
    def right_page(self):
        tenant = self.context["object"]
        vcs = tables.EvpnVCTenantTable(list(tenant.evpnvcs.all().annotate(vlan_count=Count('vlans'))), orderable=False)
        template_filename = "netbox_evpn_vc/tenant_evpn_vc.html"

        try:
            return self.render(
                template_filename, extra_context={"evpnvcs": vcs}
            )
        except ObjectDoesNotExist:
            return ""

template_extensions = [EvpnVCVLANStatus, TenantEvpnVCs]
