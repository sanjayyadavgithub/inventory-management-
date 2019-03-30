# Generated by Django 2.1.7 on 2019-03-28 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('status', models.CharField(default='SOLD', max_length=100)),
                ('issues', models.CharField(default='No issues', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('device_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventory.Device')),
            ],
            bases=('inventory.device',),
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('device_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventory.Device')),
            ],
            bases=('inventory.device',),
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('device_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventory.Device')),
            ],
            bases=('inventory.device',),
        ),
    ]