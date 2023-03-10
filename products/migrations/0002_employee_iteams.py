# Generated by Django 4.1.3 on 2023-01-28 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=100, verbose_name='Employee Name')),
                ('month', models.DateField(verbose_name='Month')),
                ('iteam_count', models.IntegerField(verbose_name='Iteam Count')),
            ],
        ),
        migrations.CreateModel(
            name='Iteams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iteam_code', models.CharField(max_length=40, verbose_name='Iteam Code')),
                ('iteam_name', models.CharField(max_length=40, verbose_name='Iteam Name')),
                ('iteam_mes_para', models.CharField(max_length=40, verbose_name='Messure')),
                ('iteam_qty', models.CharField(max_length=40, verbose_name='Iteam Qty')),
                ('image', models.CharField(max_length=40, verbose_name='Image')),
                ('supplier_name', models.CharField(max_length=40, verbose_name='Supplier Name')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('employee_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='products.employee', verbose_name='emp_name')),
            ],
            options={
                'ordering': ['iteam_name'],
            },
        ),
    ]
