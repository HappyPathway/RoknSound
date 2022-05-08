# Generated by Django 3.2.13 on 2022-05-07 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0005_alter_equipment_equipment_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentalClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('drivers_license', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='count',
        ),
        migrations.AddField(
            model_name='equipment',
            name='serial',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.CreateModel(
            name='RentalAgreement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentals.rentalclient')),
                ('package', models.ManyToManyField(to='rentals.Equipment')),
            ],
        ),
    ]
