
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0003_userlibrary'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('is_ordered', models.BooleanField(default=False)),
                ('ref_code', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.FloatField()),
                ('date_paid', models.DateTimeField(auto_now_add=True)),
                ('stipe_charge_id', models.CharField(max_length=100)),
                ('order', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='shopping_cart.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='shopping_cart.OrderItem'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
