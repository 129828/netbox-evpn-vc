# Generated by Django 4.0.3 on 2022-04-14 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_evpn_vc', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='evpnvc',
            constraint=models.UniqueConstraint(fields=('vni',), name='evpn_vc_vni'),
        ),
    ]

