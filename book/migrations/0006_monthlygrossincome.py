# Generated by Django 4.1.2 on 2022-10-14 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_alter_book_groosmarginpercent_alter_book_grossincome'),
    ]

    operations = [
        migrations.CreateModel(
            name='MOnthlyGrossIncome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grossincome', models.FloatField(null=True)),
            ],
        ),
    ]
