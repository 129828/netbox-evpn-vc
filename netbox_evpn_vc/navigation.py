from netbox.plugins import PluginMenu, PluginMenuButton, PluginMenuItem


def _add_button(link):
    return [
        PluginMenuButton(
            link=link,
            title='Add',
            icon_class='mdi mdi-plus-thick',
        )
    ]


menu = PluginMenu(
    label='EVPN',
    icon_class='mdi mdi-vpn',
    groups=[
        (
            'EVPN',
            (
                PluginMenuItem(
                    link='plugins:netbox_evpn_vc:evpnvc_list',
                    link_text='VCs',
                    buttons=_add_button('plugins:netbox_evpn_vc:evpnvc_add'),
                ),
                PluginMenuItem(
                    link='plugins:netbox_evpn_vc:evpnvcvlan_list',
                    link_text='VC-VLANs',
                    buttons=_add_button('plugins:netbox_evpn_vc:evpnvcvlan_add'),
                ),
                PluginMenuItem(
                    link='plugins:netbox_evpn_vc:evpnvctype_list',
                    link_text='VC Types',
                    buttons=_add_button('plugins:netbox_evpn_vc:evpnvctype_add'),
                ),
            ),
        )
    ],
)
