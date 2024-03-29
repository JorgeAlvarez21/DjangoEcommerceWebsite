# Generated by Django 4.1 on 2022-10-15 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('brand', models.CharField(max_length=30, null=True)),
                ('category', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('on_discount', models.BooleanField(default=0, null=True)),
                ('description', models.TextField(null=True)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(null=True, upload_to='prod-images-logos/')),
            ],
        ),
    ]
