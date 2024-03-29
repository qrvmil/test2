# Generated by Django 4.2.3 on 2023-07-22 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(choices=[('AR', 'Art'), ('SP', 'Sport'), ('CS', 'Computer Science'), ('MTH', 'Math'), ('NW', 'News'), ('ED', 'Education'), ('FD', 'Food'), ('TRV', 'Travelling'), ('AN', 'Animals'), ('MS', 'Memes'), ('TCH', 'Technologies'), ('MSC', 'Music'), ('CN', 'Cinema')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='LinkDigest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction', models.TextField(blank=True)),
                ('name', models.CharField(max_length=50)),
                ('conclusion', models.TextField(blank=True)),
                ('public', models.BooleanField(default=True)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_link_digest', to='user.profile')),
                ('saves', models.ManyToManyField(blank=True, null=True, related_name='saved_link_digest', to='user.profile')),
                ('topic', models.ManyToManyField(blank=True, to='digest.topics')),
            ],
        ),
        migrations.CreateModel(
            name='ImageDigest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction', models.TextField(blank=True)),
                ('name', models.CharField(max_length=50)),
                ('conclusion', models.TextField(blank=True)),
                ('public', models.BooleanField(default=True)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_img_digest', to='user.profile')),
                ('saves', models.ManyToManyField(blank=True, null=True, related_name='saved_img_digest', to='user.profile')),
                ('topic', models.ManyToManyField(blank=True, to='digest.topics')),
            ],
        ),
        migrations.CreateModel(
            name='DigestLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True)),
                ('description', models.TextField()),
                ('digest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='links', to='digest.linkdigest')),
            ],
        ),
        migrations.CreateModel(
            name='DigestImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='digest_images')),
                ('description', models.TextField()),
                ('digest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='digest.imagedigest')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('img_digest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='digest.imagedigest')),
                ('link_digest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='digest.linkdigest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
            ],
        ),
    ]
