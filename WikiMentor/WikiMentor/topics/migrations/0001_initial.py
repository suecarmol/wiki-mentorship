# Generated by Django 3.2.3 on 2021-05-19 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the topic', max_length=235)),
                ('description', models.TextField(help_text='A long description of that topic')),
                ('potential_mentees', models.ManyToManyField(related_name='mentees', to='users.UserProfile')),
                ('potential_mentors', models.ManyToManyField(related_name='mentors', to='users.UserProfile')),
            ],
            options={
                'verbose_name': 'topic',
                'verbose_name_plural': 'topics',
            },
        ),
    ]
