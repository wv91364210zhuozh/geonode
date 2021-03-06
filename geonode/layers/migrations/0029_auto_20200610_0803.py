# Generated by Django 2.2.13 on 2020-06-10 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layers', '0028_auto_20200610_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='featureinfo_type',
            field=models.CharField(choices=[('type_property', 'Property-Label'), ('type_href', 'HREF-Link'), ('type_image', 'Image'), ('type_video', 'Video'), ('type_audio', 'Audio')], default='type_property', help_text='specifies if the attribute should be rendered with an HTML widget on GetFeatureInfo template.', max_length=255, verbose_name='featureinfo type'),
        ),
    ]
