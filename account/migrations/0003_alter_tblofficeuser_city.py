# Generated by Django 4.1.6 on 2023-02-12 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_tbluser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblofficeuser',
            name='city',
            field=models.PositiveIntegerField(choices=[('', '-------'), (1, 'البيضاء'), (2, 'بنغازي')]),
        ),
    ]
