from django import forms
from ipam.models import VLAN
from netbox.forms import NetBoxModelBulkEditForm, NetBoxModelFilterSetForm, NetBoxModelForm
from tenancy.models import Tenant
from utilities.forms.fields import CommentField, DynamicModelChoiceField, DynamicModelMultipleChoiceField
from virtualization.models import Cluster

from .models import EvpnVC, EvpnVCType, EvpnVCVlan


class EvpnVCTypeForm(NetBoxModelForm):
    class Meta:
        model = EvpnVCType
        fields = ('name', 'description', 'tags')


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
    model = EvpnVC

    pk = forms.ModelMultipleChoiceField(
        queryset=EvpnVC.objects.all(),
        widget=forms.MultipleHiddenInput
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False
    )
    # not required: a bulk edit must be able to change other fields without touching the type
    vc_type = DynamicModelChoiceField(
        queryset=EvpnVCType.objects.all(),
        required=False
    )
    clusters = DynamicModelMultipleChoiceField(
        queryset=Cluster.objects.all(),
        required=False
    )

    fieldsets = (
        (None, ('tenant', 'vc_type', 'clusters')),
    )
    nullable_fields = ('tenant', 'clusters')


class EvpnVCFilterSetForm(NetBoxModelFilterSetForm):
    model = EvpnVC

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
        fields = ('evpn_vc', 'vlan', 'tags')


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
