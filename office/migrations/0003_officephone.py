# Generated by Django 4.1.6 on 2023-02-08 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_tbluser_user_type'),
        ('office', '0002_delete_officephone'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficePhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=14)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='office', to='account.tblofficeuser')),
            ],
        ),
    ]