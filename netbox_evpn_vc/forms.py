from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm, NetBoxModelBulkEditForm 
from utilities.forms.fields import CommentField, DynamicModelChoiceField, DynamicModelMultipleChoiceField
from ipam.models import VLAN
from tenancy.models import Tenant
from virtualization.models import Cluster
from .models import EvpnVC, EvpnVCVlan, EvpnVCType

class EvpnVCTypeForm(NetBoxModelForm):
    class Meta:
        model = EvpnVCType
        fields = ('name', 'description')

class EvpnVCTypeFilterSetForm(NetBoxModelFilterSetForm):
    model = EvpnVCType

class EvpnVCForm(NetBoxModelForm):
    comments = CommentField()
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False
    )
    vc_type = DynamicModelChoiceField(
        queryset=EvpnVCType.objects.all(),
        required=True
    )

    clusters = DynamicModelMultipleChoiceField(
        queryset=Cluster.objects.all(),
        required=False
    )

    class Meta:
        model = EvpnVC 
        fields = ('vni', 'name', 'vc_type', 'tenant', 'clusters', 'comments', 'tags')

class EvpnVCBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=EvpnVC.objects.all(),
        widget=forms.MultipleHiddenInput
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False
    )
    vc_type = DynamicModelChoiceField(
        queryset=EvpnVCType.objects.all(),
        required=True
    )
    clusters = DynamicModelMultipleChoiceField(
        queryset=Cluster.objects.all(),
        required=False
    )

    model = EvpnVC
    fieldsets = (
        (None, ('tenant','vc_type','clusters')),
    )

    class Meta:
        nullable_fields = [
            'tenant',
            'clusters',
        ]

class EvpnVCVlanForm(NetBoxModelForm):
    evpn_vc = DynamicModelChoiceField(
        queryset=EvpnVC.objects.all()
    )
    vlan = DynamicModelChoiceField(
        queryset=VLAN.objects.all(),
        required=True
    )

    class Meta:
        model = EvpnVCVlan
        fields = ('evpn_vc', 'vlan',)

class EvpnVCFilterSetForm(NetBoxModelFilterSetForm):
    model = EvpnVC

    q = forms.CharField(
        required=False,
        label='Search'
    )
    vni = forms.CharField(
        required=False,
        label='VNI'
    )
    name = forms.CharField(
        required=False,
        label='Name'
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False
    )
    vc_type = DynamicModelChoiceField(
        queryset=EvpnVCType.objects.all(),
        required=False
    )

class EvpnVCVlanFilterSetForm(NetBoxModelFilterSetForm):
    model = EvpnVCVlan

    evpn_vc = DynamicModelChoiceField(
        queryset=EvpnVC.objects.all(),
        required=False
    )
    vlan = DynamicModelChoiceField(
        queryset=VLAN.objects.all(),
        required=False
    )
