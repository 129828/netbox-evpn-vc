from extras.plugins import PluginMenuButton, PluginMenuItem, PluginMenu
from utilities.choices import ButtonColorChoices

evpnvc_type_buttons = [
    PluginMenuButton(
        link='plugins:netbox_evpn_vc:evpnvctype_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]
evpnvc_buttons = [
    PluginMenuButton(
        link='plugins:netbox_evpn_vc:evpnvc_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

evpnvcvlan_buttons = [
    PluginMenuButton(
        link='plugins:netbox_evpn_vc:evpnvcvlan_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

# menu_items = (
#     PluginMenuItem(
#         link='plugins:netbox_evpn_vc:evpnvc_list',
#         link_text='VCs',
#         buttons=evpnvc_buttons
#     ),
#     PluginMenuItem(
#         link='plugins:netbox_evpn_vc:evpnvcvlan_list',
#         link_text='VC-VLANs',
#         buttons=evpnvcvlan_buttons
#     ),
#     PluginMenuItem(
#         link='plugins:netbox_evpn_vc:evpnvctype_list',
#         link_text='VC Types',
#         buttons=evpnvc_type_buttons
#     ),
# )

menu = PluginMenu(
    label='EVPN',
    icon_class='mdi mdi-vpn',
    groups=(
        (
            'EVPN',
            (
                PluginMenuItem(
                    link='plugins:netbox_evpn_vc:evpnvc_list',
                    link_text='VCs',
                    buttons=evpnvc_buttons
                ),
                PluginMenuItem(
                    link='plugins:netbox_evpn_vc:evpnvcvlan_list',
                    link_text='VC-VLANs',
                    buttons=evpnvcvlan_buttons
                ),
                PluginMenuItem(
                    link='plugins:netbox_evpn_vc:evpnvctype_list',
                    link_text='VC Types',
                    buttons=evpnvc_type_buttons
                )
            )
        )
    )
)
