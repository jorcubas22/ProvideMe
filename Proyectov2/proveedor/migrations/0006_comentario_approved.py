# Generated by Django 2.1.7 on 2019-05-02 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0005_auto_20190502_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
