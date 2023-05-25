from os import name
from rest_framework import serializers
from api.models import News, Tag, Keywords

class TagSerializer(serializers.ModelSerializer):
    #name = serializers.ReadOnlyField(source = 'tag.name')

    class Meta:
        model = Tag
        fields = [ 'id', 'name' ]
        read_only_fields = ['id', 'name']

class KeywordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keywords
        fields = [ 'id', 'name' ]

class NewsSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many = True, read_only = True)
    keywords = KeywordsSerializer(many = True, read_only = True)

    class Meta:
        model = News
        fields = ['id', 'date', 'tags', 'keywords', 'name', 'description', 'image', 'created_at', 'updated_at' ]

    # def create(self, validated_data) -> News:
        #news_tags = Tag.objects.create(validated_data.get('tags'))
        #keywords = keywords.objects.create(**validated_data.get('keywords'))
        #news = NewsSerializer.objects.create(
        #    tags = news_tags, name = validated_data.get('name'), description = validated_data.get('description'), image = validated_data.get('image') 
        #)
        # news_tags = Tag.objects.create(validated_data.get('tags'))
        # news = NewsSerializer.objects.create(
        #     name = validated_data.get('name'), description = validated_data.get('description'), image = validated_data.get('image') 
        # )
        # news.tags.add(news_tags)
        # return News.objects.create(validated_data)
    # def create(self, validated_data):
    #     tags_data = validated_data.pop('tags')
    #     news = News.objects.create(**validated_data)
    #     for tag_data in tags_data:
    #         tag = Tag.objects.get_or_create(name=tag_data['name'])
    #         news.tags.set([tag[0]])
    #     return news
