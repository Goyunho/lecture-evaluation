# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-29 04:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='강의명')),
                ('info', models.TextField(blank=True, default='', null=True, verbose_name='설명')),
            ],
        ),
        migrations.CreateModel(
            name='Undergraduate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='학부명')),
                ('university', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.University', verbose_name='학교')),
            ],
        ),
        migrations.RemoveField(
            model_name='professor',
            name='belong',
        ),
        migrations.RemoveField(
            model_name='department',
            name='faculty',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='university',
        ),
        migrations.AddField(
            model_name='faculty',
            name='age',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='나이'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='belong',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Department', verbose_name='소속'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254, verbose_name='메일'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='phone',
            field=models.CharField(default='', max_length=20, verbose_name='전화번호'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='사진'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='교수명'),
        ),
        migrations.DeleteModel(
            name='Professor',
        ),
        migrations.AddField(
            model_name='lecture',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Faculty'),
        ),
        migrations.AddField(
            model_name='department',
            name='undergraduate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Undergraduate', verbose_name='학부'),
        ),
    ]
