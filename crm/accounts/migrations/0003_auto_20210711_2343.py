# Generated by Django 3.2.5 on 2021-07-11 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210711_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered')], max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
