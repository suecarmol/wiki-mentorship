# Generated by Django 3.2.3 on 2021-05-19 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='potential_mentees',
            field=models.ManyToManyField(null=True, related_name='mentees', to='users.UserProfile'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='potential_mentors',
            field=models.ManyToManyField(null=True, related_name='mentors', to='users.UserProfile'),
        ),
    ]