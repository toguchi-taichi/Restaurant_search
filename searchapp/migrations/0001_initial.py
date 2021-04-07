# Generated by Django 3.1.4 on 2021-01-23 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=100)),
                ('area', models.CharField(choices=[('SA11', '東京'), ('SA12', '神奈川'), ('SA13', '埼玉'), ('SA14', '千葉'), ('SA15', '茨城'), ('SA16', '栃木'), ('SA17', '群馬'), ('SA21', '滋賀'), ('SA22', '京都'), ('SA23', '大阪'), ('SA24', '兵庫'), ('SA25', '奈良'), ('SA26', '和歌山'), ('SA31', '岐阜'), ('SA32', '静岡'), ('SA33', '愛知'), ('SA34', '三重'), ('SA41', '北海道'), ('SA51', '青森'), ('SA52', '岩手'), ('SA53', '宮城'), ('SA54', '秋田'), ('SA55', '山形'), ('SA56', '福島'), ('SA61', '新潟'), ('SA62', '富山'), ('SA63', '石川'), ('SA64', '福井'), ('SA65', '山梨'), ('SA66', '長野'), ('SA71', '鳥取'), ('SA72', '島根'), ('SA73', '岡山'), ('SA74', '広島'), ('SA75', '山口'), ('SA81', '徳島'), ('SA82', '香川'), ('SA83', '愛媛'), ('SA84', '高知'), ('SA91', '福岡'), ('SA92', '佐賀'), ('SA93', '長崎'), ('SA94', '熊本'), ('SA95', '大分'), ('SA96', '宮崎'), ('SA97', '鹿児島'), ('SA98', '沖縄')], max_length=100)),
            ],
        ),
    ]