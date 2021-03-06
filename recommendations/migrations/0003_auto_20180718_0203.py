# Generated by Django 2.0.4 on 2018-07-17 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0002_recommendation_profession'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bullet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('link_name', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('recommendation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommendations.Recommendation')),
            ],
        ),
        migrations.AddField(
            model_name='bullet',
            name='recommendation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommendations.Step'),
        ),
    ]
