# Generated by Django 4.1.5 on 2023-01-23 09:02

from django.db import migrations, models
import netbox_documents.utils
import utilities.json


class Migration(migrations.Migration):

    dependencies = [
        ("netbox_documents", "0002_AddDeviceType"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="circuitdocument",
            options={
                "ordering": ("name",),
                "verbose_name": "Circuit Document",
                "verbose_name_plural": "Circuit Documents",
            },
        ),
        migrations.AlterModelOptions(
            name="devicedocument",
            options={
                "ordering": ("name",),
                "verbose_name": "Device Document",
                "verbose_name_plural": "Device Documents",
            },
        ),
        migrations.AlterModelOptions(
            name="devicetypedocument",
            options={
                "ordering": ("name",),
                "verbose_name": "Device Type Document",
                "verbose_name_plural": "Device Type Documents",
            },
        ),
        migrations.AlterModelOptions(
            name="sitedocument",
            options={
                "ordering": ("-created", "name"),
                "verbose_name": "Site Document",
                "verbose_name_plural": "Site Documents",
            },
        ),
        migrations.AddField(
            model_name="circuitdocument",
            name="external_url",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="devicedocument",
            name="external_url",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="devicetypedocument",
            name="external_url",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="sitedocument",
            name="external_url",
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name="circuitdocument",
            name="custom_field_data",
            field=models.JSONField(
                blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder
            ),
        ),
        migrations.AlterField(
            model_name="circuitdocument",
            name="document",
            field=models.FileField(
                blank=True, upload_to=netbox_documents.utils.file_upload
            ),
        ),
        migrations.AlterField(
            model_name="devicedocument",
            name="custom_field_data",
            field=models.JSONField(
                blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder
            ),
        ),
        migrations.AlterField(
            model_name="devicedocument",
            name="document",
            field=models.FileField(
                blank=True, upload_to=netbox_documents.utils.file_upload
            ),
        ),
        migrations.AlterField(
            model_name="devicetypedocument",
            name="custom_field_data",
            field=models.JSONField(
                blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder
            ),
        ),
        migrations.AlterField(
            model_name="devicetypedocument",
            name="document",
            field=models.FileField(
                blank=True, upload_to=netbox_documents.utils.file_upload
            ),
        ),
        migrations.AlterField(
            model_name="sitedocument",
            name="custom_field_data",
            field=models.JSONField(
                blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder
            ),
        ),
        migrations.AlterField(
            model_name="sitedocument",
            name="document",
            field=models.FileField(
                blank=True, upload_to=netbox_documents.utils.file_upload
            ),
        ),
    ]
