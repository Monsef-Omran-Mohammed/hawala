# Generated by Django 4.1.6 on 2023-02-11 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0004_rename_moneytransfer_tblmoneytransfer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblmoneytransfer',
            name='rejection_note',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tblmoneytransfer',
            name='note',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]