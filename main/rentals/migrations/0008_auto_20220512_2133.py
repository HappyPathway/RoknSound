# Generated by Django 3.2.13 on 2022-05-12 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0007_auto_20220512_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_status', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='equipment',
            name='rental_count',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipment',
            name='equipment_status',
            field=models.ManyToManyField(to='rentals.EquipmentStatus'),
        ),
    ]