from netbox.plugins import PluginConfig
# from .graphql import Query as EvpnQuery

class NetBoxEvpnVCConfig(PluginConfig):
    name = 'netbox_evpn_vc'
    verbose_name = 'EVPN Virtual Circuit'
    description = 'Manage EVPN Virtual Circuit'
    version = '0.2'
    base_url = 'evpn-vc'
    min_version = '3.2.0',
    # graphql_types = [EvpnQuery]

config = NetBoxEvpnVCConfig
