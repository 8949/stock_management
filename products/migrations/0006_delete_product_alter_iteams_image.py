# Generated by Django 4.1.3 on 2023-01-28 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_iteams_image_alter_iteams_iteam_code_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AlterField(
            model_name='iteams',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
