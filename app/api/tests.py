from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from api.models import News, Tag, Keywords

# Проверка новости на корректнось
class NewsTest(TestCase):
    def setUp(self):
        tag = Tag.objects.create(name="test tag")
        keyword = Keywords.objects.create(name="test keyword")
        news = News.objects.create(date="2023-05-27 03:34:00.000 +0500", name="test news", description="test description", image="test.jpg")
        news.tags.add(tag)
        news.keywords.add(keyword)

    def test_news_model(self):
        news = News.objects.get(name="test news")
        self.assertEqual(news.description, "test description")
        self.assertEqual(news.image, "test.jpg")
        self.assertEqual(news.tags.count(), 1)
        self.assertEqual(news.keywords.count(), 1)

# Проверка связи многие-ко-многим
class TagsKeywordsTest(TestCase):
    def setUp(self):
        tag1 = Tag.objects.create(name="test tag 1")
        tag2 = Tag.objects.create(name="test tag 2")
        keyword1 = Keywords.objects.create(name="test keyword 1")
        keyword2 = Keywords.objects.create(name="test keyword 2")
        news = News.objects.create(date="2023-05-27 03:34:00.000 +0500", name="test name", description="test description", image="test.jpg")
        news.tags.add(tag1)
        news.tags.add(tag2)
        news.keywords.add(keyword1)
        news.keywords.add(keyword2)

    def test_news_model(self):
        news = News.objects.get(name="test name")
        self.assertEqual(news.tags.count(), 2)
        self.assertEqual(news.keywords.count(), 2)

# Проверка автоматического заполнения поля created_at
class CreatedAtTest(TestCase):
    def setUp(self):
        tag = Tag.objects.create(name="test tag")
        keyword = Keywords.objects.create(name="test keyword")
        news = News.objects.create(date="2023-05-27 03:34:00.000 +0500", name="test name", description="test description", image="test.jpg")

    def test_news_model(self):
        news = News.objects.get(name="test name")
        self.assertIsNotNone(news.created_at)

# Проверка автоматического обновления поля updated_at
class UpdatedAtTest(TestCase):
    def setUp(self):
        tag = Tag.objects.create(name="test tag")
        keyword = Keywords.objects.create(name="test keyword")
        news = News.objects.create(date="2023-05-27 03:34:00.000 +0500", name="test name", description="test description", image="test.jpg")

    def test_news_model(self):
        news = News.objects.get(name="test name")
        news.description = "new description"
        news.save()
        self.assertIsNotNone(news.updated_at)

# Проверка авторизации в админ-панель
class AdminTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='testuser',
            email='testuser@example.com',
            password='secret')

    def test_admin_login(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('admin:index'))
        self.assertEqual(response.status_code, 200)
