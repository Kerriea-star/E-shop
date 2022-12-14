# Generated by Django 4.0.5 on 2022-08-10 08:17

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('full_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='full name')),
                ('email', models.EmailField(error_messages={'unique': 'A user with email already exists.'}, max_length=254, unique=True, verbose_name='email')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=27, null=True, region=None, unique=True, verbose_name='phone number')),
                ('role', models.CharField(choices=[('Administrator', 'Administrator'), ('Customer', 'Customer')], max_length=17, verbose_name='Role')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_admin', models.BooleanField(default=False, verbose_name='admin')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='timestamp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='bio')),
                ('profile_picture', models.ImageField(default='default.png', upload_to='profile', verbose_name='profile picture')),
                ('city', models.CharField(blank=True, max_length=47, null=True, verbose_name='city')),
                ('address', models.CharField(blank=True, max_length=87, null=True, verbose_name='address')),
                ('postal_code', models.CharField(blank=True, max_length=56, null=True, verbose_name='postal code')),
                ('town', models.CharField(blank=True, max_length=78, null=True, verbose_name='town')),
                ('estate', models.CharField(blank=True, max_length=90, null=True, verbose_name='estate')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='bio')),
                ('profile_picture', models.ImageField(default='default.png', upload_to='profile', verbose_name='profile picture')),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(max_length=50, verbose_name='last name')),
                ('county', models.CharField(blank=True, max_length=80, null=True, verbose_name='county')),
                ('town', models.CharField(blank=True, max_length=80, null=True, verbose_name='town')),
                ('estate', models.CharField(blank=True, max_length=90, null=True, verbose_name='estate')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
