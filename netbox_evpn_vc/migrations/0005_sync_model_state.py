from django.db import migrations, models


class Migration(migrations.Migration):
    """State-only sync: no schema changes (null on M2M is ignored by Django,
    ordering is not a DB attribute)."""

    dependencies = [
        ('netbox_evpn_vc', '0004_add_new_cluster_to_model'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evpnvctype',
            options={'ordering': ['name'], 'verbose_name': 'VC type', 'verbose_name_plural': 'VC types'},
        ),
        migrations.AlterField(
            model_name='evpnvc',
            name='clusters',
            field=models.ManyToManyField(blank=True, related_name='evpn_vcs', to='virtualization.cluster'),
        ),
    ]
