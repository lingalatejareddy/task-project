# Generated by Django 3.1.2 on 2020-10-03 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('development', 'Development'), ('automation', 'Automation'), ('testing', 'Testing'), ('supporting', 'Supporting'), ('admin', 'Admin')], max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(choices=[('associate', 'Associate'), ('softwareengineer', 'Softywareengineer'), ('software', 'Softwarese'), ('tl', 'Tl'), ('manager', 'Manager')], max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='empac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elogin', models.DateTimeField()),
                ('elogout', models.DateTimeField()),
                ('breakhourstart', models.DateTimeField()),
                ('breakhourend', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=64)),
                ('eno', models.IntegerField()),
                ('esal', models.IntegerField()),
                ('etech', models.CharField(max_length=64)),
                ('eaddr', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('emobileno', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=64)),
                ('cemployees', models.IntegerField()),
                ('cid', models.IntegerField()),
                ('caddr', models.CharField(max_length=64)),
                ('cedate', models.DateField()),
            ],
        ),
    ]
