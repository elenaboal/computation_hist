# Generated by Django 2.1.5 on 2019-01-23 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_comp_hist', '0012_organization_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='cced_organization',
            field=models.ManyToManyField(blank=True, related_name='cced_organization', to='dj_comp_hist.Organization'),
        ),
        migrations.AddField(
            model_name='document',
            name='cced_person',
            field=models.ManyToManyField(blank=True, related_name='cced_person', to='dj_comp_hist.Person'),
        ),
    ]
