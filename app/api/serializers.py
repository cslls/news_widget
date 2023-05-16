from rest_framework import serializers
from api.models import News, Tag, Keywords

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [ 'id', 'name' ]

class KeywordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keywords
        fields = [ 'id', 'name' ]

class NewsSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many = True)
    keywords = KeywordsSerializer(many = True)

    class Meta:
        model = News
        fields = ['id', 'date', 'tags', 'keywords', 'name', 'description', 'image', 'created_at', 'updated_at' ]
