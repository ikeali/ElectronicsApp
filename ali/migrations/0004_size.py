# Generated by Django 4.2 on 2023-04-21 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ali', '0003_product_featured_product_popular'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wearsize', models.CharField(max_length=20)),
            ],
        ),
    ]
