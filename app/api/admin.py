from django.contrib import admin
from api.models import News, Tag, Keywords 

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Keywords)
class KeywordsAdmin(admin.ModelAdmin):
    pass
