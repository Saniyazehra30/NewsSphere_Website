# Generated by Django 5.1.1 on 2024-11-27 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(null=True, upload_to='static/category/')),
                ('title', models.CharField(max_length=40, null=True)),
                ('descrp', models.TextField(null=True)),
            ],
        ),
    ]
