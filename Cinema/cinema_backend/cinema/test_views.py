from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model
from .genre_views import GenreListView, GenreCreateView, GenreDeleteView
from django.contrib.auth.models import AnonymousUser

from .models import Genre

User = get_user_model()


class GenreViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(
            username='bindeep',
            password='bindeep123',
            is_staff=True,
            is_superuser=True)

    def test_unauthroized_user_genre_list(self):
        Genre.objects.create(name='Comedy')
        list_url = reverse("movie:genre_list")
        request = self.factory.get(list_url)
        request.user = AnonymousUser()
        response = GenreListView.as_view()(request)
        try:
            self.assertEqual(response.status_code, 200)
        except:
            self.assertEquals(response.status_code, 302)
            self.fail('Authorization is required')

    def test_authroized_user_genre_list(self):
        Genre.objects.create(name='Comedy')
        list_url = reverse("movie:genre_list")
        request = self.factory.get(list_url)
        request.user = self.user
        response = GenreListView.as_view()(request)
        try:
            self.assertEqual(response.status_code, 200)
        except:
            self.assertEquals(response.status_code, 302)
            self.fail('Authorization is required')

    def test_unauthroized_user_genre_delete(self):
        obj = Genre.objects.create(name='Comedy')
        delete_url = reverse("movie:genre_delete", kwargs={"pk": obj.pk})
        request = self.factory.get(delete_url)
        request.user = AnonymousUser()
        response = GenreDeleteView.as_view()(request, pk=obj.pk)
        try:
            self.assertEqual(response.status_code, 200)
            self.assertEquals(Genre.objects.count(), 0)
        except:
            self.assertEquals(response.status_code, 302)
            self.fail('Authorization is required')

    def test_authroized_user_genre_delete(self):
        obj = Genre.objects.create(name='Comedy')
        delete_url = reverse("movie:genre_delete", kwargs={"pk": obj.pk})
        request = self.factory.get(delete_url)
        request.user = self.user
        response = GenreDeleteView.as_view()(request, pk=obj.pk)
        print(response.status_code)
        try:
            self.assertEqual(response.status_code, 200)
        except:
            self.assertEquals(response.status_code, 302)
            self.fail('Authorization is required')

    def test_unauthorized_user_genre_create(self):
        data = {
            'name': 'Comedy'
        }
        create_url = reverse('movie:genre_create')
        request = self.factory.post(create_url, data)
        request.user = AnonymousUser()
        response = GenreCreateView.as_view()(request)
        try:
            self.assertEqual(response.status_code, 200)
            self.assertEquals(Genre.objects.count(), 1)
        except:
            self.assertEquals(response.status_code, 302)
            self.fail('Authorization is required')

    def test_authorized_user_genre_create(self):
        data = {
            'name': 'Comedy'
        }
        create_url = reverse('movie:genre_create')
        request = self.factory.post(create_url, data)
        request.user = self.user
        response = GenreCreateView.as_view()(request)
        try:
            self.assertEqual(response.status_code, 200)
            self.assertEquals(Genre.objects.count(), 1)
        except:
            self.assertEquals(response.status_code, 302)
            self.fail('Authorization is required')
