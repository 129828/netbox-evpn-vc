from django.db.models import Count
from netbox.views import generic

from . import filtersets, forms, models, tables


# VC types

class EvpnVCTypeView(generic.ObjectView):
    queryset = models.EvpnVCType.objects.all()


class EvpnVCTypeListView(generic.ObjectListView):
    queryset = models.EvpnVCType.objects.all()
    table = tables.EvpnVCTypeTable
    filterset = filtersets.EvpnVCTypeFilterSet
    filterset_form = forms.EvpnVCTypeFilterSetForm


class EvpnVCTypeEditView(generic.ObjectEditView):
    queryset = models.EvpnVCType.objects.all()
    form = forms.EvpnVCTypeForm


class EvpnVCTypeDeleteView(generic.ObjectDeleteView):
    queryset = models.EvpnVCType.objects.all()


class EvpnVCTypeBulkDeleteView(generic.BulkDeleteView):
    queryset = models.EvpnVCType.objects.all()
    filterset = filtersets.EvpnVCTypeFilterSet
    table = tables.EvpnVCTypeTable


# EVPN VCs

class EvpnVCView(generic.ObjectView):
    queryset = models.EvpnVC.objects.select_related('tenant', 'vc_type').prefetch_related('clusters')

    def get_extra_context(self, request, instance):
        table = tables.EvpnVCVlanTable(instance.vlans.select_related('vlan'))
        table.configure(request)

        return {
            'vlans_table': table,
        }


class EvpnVCListView(generic.ObjectListView):
    # distinct=True: the clusters join (search/filter) would otherwise multiply the vlan count
    queryset = models.EvpnVC.objects.select_related('tenant', 'vc_type').prefetch_related('clusters').annotate(
        vlan_count=Count('vlans', distinct=True)
    )
    table = tables.EvpnVCTable
    filterset = filtersets.EvpnVCFilterSet
    filterset_form = forms.EvpnVCFilterSetForm


class EvpnVCEditView(generic.ObjectEditView):
    queryset = models.EvpnVC.objects.all()
    form = forms.EvpnVCForm


class EvpnVCBulkEditView(generic.BulkEditView):
    queryset = models.EvpnVC.objects.all()
    filterset = filtersets.EvpnVCFilterSet
    table = tables.EvpnVCTable
    form = forms.EvpnVCBulkEditForm


class EvpnVCDeleteView(generic.ObjectDeleteView):
    queryset = models.EvpnVC.objects.all()


class EvpnVCBulkDeleteView(generic.BulkDeleteView):
    queryset = models.EvpnVC.objects.all()
    filterset = filtersets.EvpnVCFilterSet
    table = tables.EvpnVCTable


# VNI to VLAN connections

class EvpnVCVlanView(generic.ObjectView):
    queryset = models.EvpnVCVlan.objects.select_related('evpn_vc', 'vlan')


class EvpnVCVlanListView(generic.ObjectListView):
    queryset = models.EvpnVCVlan.objects.select_related('evpn_vc', 'vlan')
    table = tables.EvpnVCVlanListTable
    filterset = filtersets.EvpnVCVlanFilterSet
    filterset_form = forms.EvpnVCVlanFilterSetForm


class EvpnVCVlanEditView(generic.ObjectEditView):
    queryset = models.EvpnVCVlan.objects.all()
    form = forms.EvpnVCVlanForm


class EvpnVCVlanDeleteView(generic.ObjectDeleteView):
    queryset = models.EvpnVCVlan.objects.all()


class EvpnVCVlanBulkDeleteView(generic.BulkDeleteView):
    queryset = models.EvpnVCVlan.objects.all()
    filterset = filtersets.EvpnVCVlanFilterSet
    table = tables.EvpnVCVlanListTable
