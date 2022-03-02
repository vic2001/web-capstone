
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_userlibrary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlibrary',
            name='books',
            field=models.ManyToManyField(blank=True, to='books.Book'),
        ),
    ]
