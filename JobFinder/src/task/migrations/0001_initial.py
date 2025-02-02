# Generated by Django 4.2.17 on 2024-12-14 14:57

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
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('taskDescription', models.TextField(default='', max_length=1500)),
                ('category', models.CharField(choices=[('home_repair', 'Home Repair'), ('delivery', 'Delivery'), ('tutoring', 'Tutoring'), ('other', 'Other')], default='other', max_length=50)),
                ('location', models.CharField(blank=True, default='', max_length=100)),
                ('budget', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('deadline', models.DateTimeField(null=True)),
                ('publishedAt', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
