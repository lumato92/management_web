# Generated by Django 4.1 on 2022-08-24 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='employe_active',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='employee_adress',
            new_name='adress',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='employee_cuil',
            new_name='cuil',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='employee_dni',
            new_name='dni',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='employee_dob',
            new_name='dob',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='employee_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='employee_lastname',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='employee_mobile',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='employee_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='employee_nationality',
            new_name='nationality',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='employee_phone',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='employee_place',
            new_name='place',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='employee_position',
            new_name='position',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='employee_salary',
            new_name='salary',
        ),
        migrations.RenameField(
            model_name='employeeterm',
            old_name='term_enddate',
            new_name='enddate',
        ),
        migrations.RenameField(
            model_name='employeeterm',
            old_name='term_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='employeeterm',
            old_name='term_salary',
            new_name='salary',
        ),
        migrations.RenameField(
            model_name='position',
            old_name='position_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='position',
            old_name='position_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='workplace',
            old_name='place_adress',
            new_name='adress',
        ),
        migrations.RenameField(
            model_name='workplace',
            old_name='place_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='workplace',
            old_name='place_phone',
            new_name='phone',
        ),
    ]
