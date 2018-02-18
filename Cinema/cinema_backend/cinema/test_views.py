# from django.test import TestCase, RequestFactory
# from django.urls import reverse
# from django.contrib.auth import get_user_model
# # from .genre_views import GenreListView, GenreCreateView, GenreDeleteView
# from .movie_views import (
#     MovieListView,
#     MovieCreateView,
#     MovieDetailView,
#     MovieUpdateView,
#     MovieSearchView,
#     MovieDeleteView)
# from django.contrib.auth.models import AnonymousUser

# from .models import Genre, Movie

# User = get_user_model()


# class GenreViewTestCase(TestCase):

#     def setUp(self):
#         self.factory = RequestFactory()
#         self.user = User.objects.create(
#             username='bindeep',
#             password='bindeep123',
#             is_staff=True,
#             is_superuser=True)

#     def test_unauthroized_user_genre_list(self):
#         Genre.objects.create(name='Comedy')
#         list_url = reverse("movie:genre_list")
#         request = self.factory.get(list_url)
#         request.user = AnonymousUser()
#         response = GenreListView.as_view()(request)
#         try:
#             self.assertEqual(response.status_code, 200)
#         except:
#             self.assertEquals(response.status_code, 302)
#             self.fail('Authorization is required')

#     def test_authroized_user_genre_list(self):
#         Genre.objects.create(name='Comedy')
#         list_url = reverse("movie:genre_list")
#         request = self.factory.get(list_url)
#         request.user = self.user
#         response = GenreListView.as_view()(request)
#         try:
#             self.assertEqual(response.status_code, 200)
#         except:
#             self.assertEquals(response.status_code, 302)
#             self.fail('Authorization is required')

#     def test_unauthroized_user_genre_delete(self):
#         obj = Genre.objects.create(name='Comedy')
#         delete_url = reverse("movie:genre_delete", kwargs={"pk": obj.pk})
#         request = self.factory.get(delete_url)
#         request.user = AnonymousUser()
#         response = GenreDeleteView.as_view()(request, pk=obj.pk)
#         try:
#             self.assertEqual(response.status_code, 200)
#             self.assertEquals(Genre.objects.count(), 0)
#         except:
#             self.assertEquals(response.status_code, 302)
#             self.fail('Authorization is required')

#     def test_authroized_user_genre_delete(self):
#         obj = Genre.objects.create(name='Comedy')
#         delete_url = reverse("movie:genre_delete", kwargs={"pk": obj.pk})
#         request = self.factory.get(delete_url)
#         request.user = self.user
#         response = GenreDeleteView.as_view()(request, pk=obj.pk)
#         print(response.status_code)
#         try:
#             self.assertEqual(response.status_code, 200)
#         except:
#             self.assertEquals(response.status_code, 302)
#             self.fail('Authorization is required')

#     def test_unauthorized_user_genre_create(self):
#         data = {
#             'name': 'Comedy'
#         }
#         create_url = reverse('movie:genre_create')
#         request = self.factory.post(create_url, data)
#         request.user = AnonymousUser()
#         response = GenreCreateView.as_view()(request)
#         try:
#             self.assertEqual(response.status_code, 200)
#             self.assertEquals(Genre.objects.count(), 1)
#         except:
#             self.assertEquals(response.status_code, 302)
#             self.fail('Authorization is required')

#     def test_authorized_user_genre_create(self):
#         data = {
#             'name': 'Comedy'
#         }
#         create_url = reverse('movie:genre_create')
#         request = self.factory.post(create_url, data)
#         request.user = self.user
#         response = GenreCreateView.as_view()(request)
#         try:
#             self.assertEqual(response.status_code, 200)
#             self.assertEquals(Genre.objects.count(), 1)
#         except:
#             self.assertEquals(response.status_code, 302)
#             self.fail('Authorization is required')


# class MovieViewTestCase(TestCase):

#     def setUp(self):
#         self.factory = RequestFactory()
#         self.user = User.objects.create_user(
#             username='bindeep',
#             password='bindeep123',
#             is_staff=True,
#             is_superuser=True)

#     def create_movie(self, **kwargs):
#         genre_obj = Genre.objects.create(name='Comedy')
#         return Movie.objects.create(
#             name='test1',
#             release_date='2018-10-10',
#             genre=genre_obj,
#             poster='media/posters/coco.jpg'
#         )

#     def movie_list_testing(self, movie_name):
#         list_url = reverse('movie:movie-list')
#         request = self.factory.get(list_url)
#         request.user = AnonymousUser()
#         response = MovieListView.as_view()(request)
#         html = response.content.decode('utf8')
#         self.assertEquals(response.status_code, 200)
#         self.assertIn(movie_name, html)

#     def test_movie_list(self):
#         self.create_movie()
#         self.movie_list_testing(movie_name='test1')

#     def test_movie_create_with_unauthorized_user(self):
#         genre_obj = Genre.objects.create(name='Comedy')
#         data = {
#             'name': 'coco',
#             'release_date': '2019-10-10',
#             'genre': genre_obj
#         }
#         create_url = reverse('movie:movie-create')
#         request = self.factory.post(create_url)
#         request.user = AnonymousUser()
#         response = MovieCreateView.as_view()(request, data)
#         self.assertNotEquals(response.status_code, 200)

#     def test_movie_create_with_authorised_user(self):
#         genre_obj = Genre.objects.create(name='Comedy')
#         data = {
#             'name': 'coco',
#             'release_date': '2019-10-10',
#             'genre': genre_obj
#         }
#         create_url = reverse('movie:movie-create')
#         request = self.factory.post(create_url)
#         request.user = self.user
#         response = MovieCreateView.as_view()(request, data)
#         self.assertEquals(response.status_code, 200)
#         # self.movie_list_testing('coco')

#     def test_movie_detail(self):
#         movie_data_obj = self.create_movie()
#         detail_url = reverse('movie:movie-detail', kwargs={'slug': movie_data_obj.slug})
#         request = self.factory.get(detail_url)
#         request.user = AnonymousUser()
#         response = MovieDetailView.as_view()(request, slug=movie_data_obj.slug)
#         self.assertEquals(response.status_code, 200)
#         html = response.content.decode('utf8')
#         self.assertIn('test1', html)

#     def test_movie_update_with_unauthorized_user(self):
#         movie_data_obj = self.create_movie()
#         data = {
#             'name': 'Dodo'
#         }
#         update_url = reverse('movie:movie-detail', kwargs={'slug': movie_data_obj.slug})
#         request = self.factory.post(update_url)
#         request.user = AnonymousUser()
#         response = MovieUpdateView.as_view()(request, data, slug=movie_data_obj.slug)
#         self.assertNotEquals(response.status_code, 200)

#     def test_movie_update_with_authorized_user(self):
#         movie_data_obj = self.create_movie()
#         data = {
#             'name': 'Dodo'
#         }
#         update_url = reverse('movie:movie-detail', kwargs={'slug': movie_data_obj.slug})
#         request = self.factory.post(update_url)
#         request.user = self.user
#         response = MovieUpdateView.as_view()(request, data, slug=movie_data_obj.slug)
#         self.assertEquals(response.status_code, 200)

#     def test_movie_search_view(self):
#         self.create_movie()
#         self.create_movie(name='test2')
#         search_url = reverse('movie:movie_search')
#         request = self.factory.get(search_url)
#         response = MovieSearchView.as_view()(request, data={'name': 'test1'})
#         self.assertEquals(response.status_code, 200)

#     def test_movie_delete_with_unauthorised_user(self):
#         movie_obj = self.create_movie()
#         delete_url = reverse('movie:movie-delete', kwargs={'pk': movie_obj.pk})
#         request = self.factory.post(delete_url)
#         request.user = AnonymousUser()
#         response = MovieDeleteView.as_view()(request, pk=movie_obj.pk)
#         self.assertNotEquals(response.status_code, 200)

#     def test_movie_delete_with_authorised_user(self):
#         movie_data_obj = self.create_movie()
#         delete_url = reverse('movie:movie-delete', kwargs={'pk': movie_data_obj.pk})
#         request = self.factory.post(delete_url)
#         request.user = self.user
#         response = MovieDeleteView.as_view()(request, pk=movie_data_obj.pk)
#         print(response.status_code)
#         self.assertEquals(response.status_code, 200)
