# Generated by Django 5.1.1 on 2024-10-13 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30, null=True)),
                ('Email', models.EmailField(max_length=50, null=True)),
                ('Mobile', models.CharField(max_length=14, null=True)),
                ('Message', models.TextField(null=True)),
            ],
        ),
    ]
