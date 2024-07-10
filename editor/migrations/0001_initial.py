# Generated by Django 5.0.6 on 2024-06-29 09:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('desc', models.TextField()),
                ('id_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.attributetype')),
            ],
        ),
        migrations.CreateModel(
            name='EntityField',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.attribute')),
                ('id_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.entity')),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_child', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='editor.entity')),
                ('id_parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='editor.entity')),
            ],
        ),
    ]