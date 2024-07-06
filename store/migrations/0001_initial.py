# Generated by Django 5.0.6 on 2024-06-28 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='any_name', max_length=200)),
                ('gategory', models.TextField(choices=[('boys', 'boys'), ('girls', 'girls')], max_length=100)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('image', models.ImageField(upload_to='photos/%y/%m/%d')),
            ],
        ),
    ]
