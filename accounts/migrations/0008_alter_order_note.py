# Generated by Django 4.1.3 on 2022-12-30 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_order_note_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=200, null=True),
        ),
    ]