# Generated by Django 5.1.7 on 2025-03-21 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('women', 'Women'), ('kids', 'Kids')], max_length=20)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
