# Generated by Django 4.1.1 on 2022-10-11 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50, unique=True)),
                ('product_image_path', models.CharField(max_length=100, unique=True)),
                ('recommended_price', models.IntegerField()),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=97)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.BinaryField(unique=True)),
                ('amount', models.IntegerField()),
                ('fp', models.CharField(max_length=100, unique=True)),
                ('used', models.BooleanField(default=False)),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='LegacySite.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LegacySite.user')),
            ],
        ),
    ]
