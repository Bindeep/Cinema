# from django.test import TestCase
# from cinema.models import Genre, Movie, Tag, UserProfile, MovieRating
# from django.contrib.auth import get_user_model

# User = get_user_model()


# class GenreModelTestCase(TestCase):

#     def setUp(self):
#         Genre.objects.create(name='Action')

#     def test_genre_create(self):
#         self.assertEquals(Genre.objects.count(), 1)

#     def test_genre_name(self):
#         obj = Genre.objects.first()
#         self.assertEquals(obj.name, 'Action')

#     def test_genre_update(self):
#         obj = Genre.objects.first()
#         obj.name = 'Comdey'
#         obj.save()
#         self.assertEquals(Genre.objects.count(), 1)
#         self.assertEquals(obj.name, 'Comdey')

#     def test_genre_delete(self):
#         Genre.objects.first().delete()
#         self.assertEquals(Genre.objects.count(), 0)


# class MovieModelTestCase(TestCase):

#     def setUp(self):
#         Genre.objects.create(name='Comedy')

#     def create_movie(self, **kwargs):
#         obj = Genre.objects.first()
#         return Movie.objects.create(genre=obj, **kwargs)

#     def test_movie_create_with_providing_required_fields(self):
#         movie_obj = self.create_movie(name='New Movie', release_date='2018-7-20')
#         self.assertEquals(Movie.objects.count(), 1)
#         self.assertEquals(movie_obj.genre.name, 'Comedy')

#     def test_movie_create_without_providing_required_field(self):
#         try:
#             movie_obj = self.create_movie(name='New Movie')
#             movie_obj.clean_fields()
#         except:
#             self.fail('Release Date is required')

#     def test_working_of_pre_save_to_create_slug(self):
#         movie_obj = self.create_movie(name='New Movie', release_date='2018-7-20')
#         self.assertIsNotNone(movie_obj.slug)

#     def test_uniqueness_of_slug_of_two_movies_of_same_name(self):
#         movie_obj1 = self.create_movie(name='New Movie', release_date='2018-4-6')
#         movie_obj2 = self.create_movie(name='New Movie', release_date='2018-4-6')
#         self.assertEquals(Movie.objects.count(), 2)
#         self.assertNotEqual(movie_obj1.slug, movie_obj2.slug)


# class TagModelTestCase(TestCase):

#     def create_tag(self):
#         return Tag.objects.create(tag_name='superhero')

#     def test_tag_create(self):
#         tag_obj = self.create_tag()
#         self.assertEquals(Tag.objects.count(), 1)
#         self.assertEquals(tag_obj.tag_name, 'superhero')

#     def test_tag_association_with_movie(self):
#         genre_obj = Genre.objects.create(name='Comedy')
#         movie_obj = Movie.objects.create(
#             name='New Movie',
#             slug='new-movie',
#             genre=genre_obj,
#             release_date='2018-10-10'
#         )
#         tag_obj = self.create_tag()
#         tag_obj.movie.add(movie_obj)
#         desired_movie_tag = Tag.objects.filter(movie__name='New Movie').get()
#         self.assertEquals(desired_movie_tag.tag_name, 'superhero')


# class UserProfilerTestCase(TestCase):

#     def setUp(self):
#         User.objects.create_user(username='first1', password='first123')

#     def create_user_profile(self, **kwargs):
#         user = User.objects.first()
#         return UserProfile.objects.create(
#             owner=user,
#             gender='Male',
#             location='kathmandu',
#             is_rated=True,
#             **kwargs)

#     def test_user_profile_create(self):
#         profile_obj = self.create_user_profile(
#             phone_number=123123,
#         )
#         self.assertEquals(UserProfile.objects.count(), 1)
#         self.assertEquals(profile_obj.phone_number, 123123)

#     def test_user_profile_create_without_required_fields(self):
#         try:
#             self.create_user_profile()
#         except:
#             self.fail('Phone number is required')

#     def test_uniqueness_of_phone_number(self):
#         try:
#             self.create_user_profile(phone_number=123123)
#             self.create_user_profile(phone_number=123123)
#         except:
#             self.fail('Phone number must be unique')

#     def test_single_user_with_multiple_profile(self):
#         user = User.objects.first()
#         try:
#             UserProfile.objects.create(owner=user, phone_number=1234)
#             UserProfile.objects.create(owner=user, phone_number=3456)
#         except:
#             self.fail('Single user is assocaited to single profile only')

#     def test_integer_constraint_of_phone_number(self):
#         try:
#             self.create_user_profile(phone_number='adcd')
#         except:
#             self.fail('number must be an integer value')

#     def test_deletion_of_user_profile_while_deleting_user(self):
#         user = User.objects.first()
#         self.create_user_profile(phone_number=12345)
#         self.assertEquals(User.objects.count(), 1)
#         self.assertEquals(UserProfile.objects.count(), 1)
#         user.delete()
#         self.assertEquals(UserProfile.objects.count(), 0)


# class MovieRatingModelTest(TestCase):

#     def setUp(self):
#         User.objects.create_user(username='first1', password='first123')
#         genre_obj = Genre.objects.create(name='Comedy')
#         Movie.objects.create(
#             name='New Movie',
#             genre=genre_obj,
#             release_date='2018-10-10'
#         )

#     def create_rating(self, **kwargs):
#         movie_obj = Movie.objects.first()
#         user_obj = User.objects.first()
#         return MovieRating.objects.create(movie=movie_obj, user=user_obj, **kwargs)

#     def test_rating_create(self):
#         rating_obj = self.create_rating(rating=3)
#         self.assertEquals(MovieRating.objects.count(), 1)
#         self.assertEquals(rating_obj.rating, 3)

#     def test_rating_assocation_with_movie(self):
#         self.create_rating(rating=3)
#         rating_obj = MovieRating.objects.filter(movie__name='New Movie').get()
#         self.assertEquals(rating_obj.rating, 3)

#     def test_rating_association_with_user(self):
#         self.create_rating(rating=3)
#         rating_obj = MovieRating.objects.filter(user__username='first1').get()
#         self.assertEquals(rating_obj.rating, 3)

#     def test_if_single_user_can_give_multiple_rating_on_multiple_movie(self):
#         movie_obj = Movie.objects.first()
#         user_obj1 = User.objects.first()
#         user_obj2 = User.objects.create_user(username='second', password='second123')
#         try:
#             rating_obj1 = MovieRating.objects.create(movie=movie_obj, user=user_obj1, rating=3)
#             rating_obj2 = MovieRating.objects.create(movie=movie_obj, user=user_obj2, rating=2)
#             self.assertNotEqual(rating_obj1, rating_obj2)
#         except:
#             self.fail('Single movie cannot have multiple rating')
