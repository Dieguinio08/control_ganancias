# Generated by Django 4.1.5 on 2023-05-27 11:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ganancias", "0007_periododeduccionincrementada_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="topevalor",
            options={
                "ordering": ["-period", "tope"],
                "verbose_name_plural": "Topes - Valores",
            },
        ),
        migrations.AlterUniqueTogether(
            name="periododeduccionincrementada",
            unique_together={("validity_from", "validity_to")},
        ),
    ]
