# Generated by Django 4.1.6 on 2023-02-16 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_tblofficeuser_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblofficeuser',
            name='city',
            field=models.PositiveIntegerField(blank=True, choices=[('', '-------'), (1, 'البيضاء'), (2, 'بنغازي')], default=1, null=True),
        ),
    ]
