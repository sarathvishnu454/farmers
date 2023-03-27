# Generated by Django 3.2.17 on 2023-02-10 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0003_farmers'),
    ]

    operations = [
        migrations.CreateModel(
            name='articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image1')),
                ('description', models.CharField(max_length=300)),
                ('date', models.DateField()),
            ],
        ),
    ]
