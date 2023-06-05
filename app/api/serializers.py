from os import name
from rest_framework import serializers
from api.models import News, Tag, Keywords

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [ 'id', 'name' ]
        read_only_fields = ['id', 'name']

class KeywordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keywords
        fields = [ 'id', 'name' ]

class NewsSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format='%d.%m.%y %H:%M')
    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='name'
     )
    keywords = serializers.SlugRelatedField(
        many=True,
        queryset=Keywords.objects.all(),
        slug_field='name'
     )
    created_at = serializers.DateTimeField(format='%d.%m.%y %H:%M', read_only = True)
    updated_at = serializers.DateTimeField(format='%d.%m.%y %H:%M', read_only = True)


    class Meta:
        model = News
        fields = ['id', 'date', 'tags', 'keywords', 'name', 'description', 'image', 'created_at', 'updated_at' ]

