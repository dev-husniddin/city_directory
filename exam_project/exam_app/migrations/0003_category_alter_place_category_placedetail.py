# Generated by Django 4.2.4 on 2023-08-13 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0002_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='exam_app.placetype')),
            ],
        ),
        migrations.AlterField(
            model_name='place',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_app.placetype'),
        ),
        migrations.CreateModel(
            name='PlaceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_app.category')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_app.place')),
            ],
        ),
    ]
