# Generated by Django 2.2 on 2020-09-01 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=50)),
                ('address', models.CharField(blank=True, default=' ', max_length=50, null=True)),
                ('city', models.CharField(default=' ', max_length=50)),
                ('state', models.CharField(default='NE', max_length=50)),
                ('zipcode', models.CharField(default='00000', max_length=10)),
                ('email', models.EmailField(default=' ', max_length=100)),
                ('cell_phone', models.CharField(default='(402)000-0000', max_length=50)),
                ('acct_number', models.CharField(blank=True, default='00000', max_length=50, null=True)),
                ('notes', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]