# Generated by Django 2.2.17 on 2021-01-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='Images/')),
                ('Title', models.CharField(max_length=200)),
                ('Text', models.TextField()),
                ('Link', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'doctorly',
            },
        ),
    ]
