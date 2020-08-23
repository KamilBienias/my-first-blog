# Generated by Django 3.0.2 on 2020-08-22 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostAndMask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_octet_1', models.DecimalField(decimal_places=0, max_digits=3)),
                ('host_octet_2', models.DecimalField(decimal_places=0, max_digits=3)),
                ('host_octet_3', models.DecimalField(decimal_places=0, max_digits=3)),
                ('host_octet_4', models.DecimalField(decimal_places=0, max_digits=3)),
                ('mask_octet_1', models.DecimalField(decimal_places=0, max_digits=3)),
                ('mask_octet_2', models.DecimalField(decimal_places=0, max_digits=3)),
                ('mask_octet_3', models.DecimalField(decimal_places=0, max_digits=3)),
                ('mask_octet_4', models.DecimalField(decimal_places=0, max_digits=3)),
            ],
        ),
    ]
