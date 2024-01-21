# Generated by Django 4.2.3 on 2023-07-22 11:28

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='users_images')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('age', models.IntegerField(default=0)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('follows', models.ManyToManyField(blank=True, related_name='followed_by', to='user.profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
