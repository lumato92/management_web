# Generated by Django 4.1 on 2022-08-25 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
