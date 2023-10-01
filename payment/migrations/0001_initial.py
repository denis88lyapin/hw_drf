# Generated by Django 4.2.5 on 2023-09-29 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты')),
                ('obj_paid', models.CharField(blank=True, choices=[('course', 'Оплачен курс'), ('lesson', 'Оплачен урок')], max_length=20, null=True, verbose_name='оплачен курс или урок')),
                ('payment_amount', models.PositiveIntegerField(verbose_name='сумма оплаты')),
                ('method', models.CharField(choices=[('cash', 'наличными'), ('transfer', 'перевод')], max_length=20, verbose_name='способ оплаты:')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
        ),
    ]