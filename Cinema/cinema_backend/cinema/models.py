from django.db import models
from django.urls import reverse
from slugify import unique_slugify
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    genre = models.ForeignKey(Genre, related_name='genre', on_delete=models.DO_NOTHING)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    run_time = models.CharField(max_length=15)
    cast = models.TextField()
    slug = models.SlugField(unique=True, blank=True, max_length=50, null=True)
    poster = models.ImageField(upload_to='posters', null=True)
    youtube_link = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self):
        self.slug = unique_slugify(self.name)
        super().save()

    def get_absolute_url(self):
        return reverse('movie:movie-detail', kwargs={'slug': self.slug})

    @property
    def get_user_rating(self):
        movie_object = Movie.objects.get(slug=self.slug)
        user_ratings_dict = movie_object.ratedmovie.all().values('user__username', 'rating')
        user_ratings_list = []
        user_ratings = ''
        for item in user_ratings_dict:
            user_ratings +='<li>' + item['user__username'] + ' has give rating of ' + str(item['rating']) + '</li>'
            user_ratings_list = user_ratings
        return user_ratings_list

    def star_percentage(self, rating):
        movie_object = Movie.objects.get(slug=self.slug)
        rated_movie_list = movie_object.ratedmovie.all()
        total_voters = rated_movie_list.count()
        if total_voters != 0:
            filtered_rating = rated_movie_list.filter(rating=rating).count()
            rating_percentage = (filtered_rating / total_voters) * 100
            return rating_percentage
        else:
            rating_percentage = 0
            return rating_percentage

    @property
    def total_voters(self):
        movie_object = Movie.objects.get(slug=self.slug)
        rated_movie_list = movie_object.ratedmovie.all()
        total_voters = rated_movie_list.count()
        return total_voters

    @property
    def one_star_percentage(self):
        return self.star_percentage(rating=1)

    @property
    def two_star_percentage(self):
        return self.star_percentage(rating=2)

    @property
    def three_star_percentage(self):
        return self.star_percentage(rating=3)

    @property
    def four_star_percentage(self):
        return self.star_percentage(rating=4)

    @property
    def five_star_percentage(self):
        return self.star_percentage(rating=5)

    @property
    def get_rating(self):
        movie_object = Movie.objects.get(slug=self.slug)
        rated_movie_list = movie_object.ratedmovie.all()
        total_voters = rated_movie_list.count()
        total_movie_rating = 0
        if total_voters != 0:
            for rating in range(1, 6):
                total_movie_rating += (rated_movie_list.filter(rating=rating).count()) * rating
            movie_rating = total_movie_rating / total_voters
            return movie_rating
        else:
            movie_rating = 0
            return movie_rating


class Tag(models.Model):
    movie = models.ManyToManyField(Movie, related_name='movie')
    tag_name = models.CharField(max_length=30)

    def __str__(self):
        return self.tag_name


class UserProfile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.BigIntegerField(unique=True, default=0)
    gender = models.CharField(
        max_length=6, choices=(('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')))
    location = models.CharField(max_length=30)
    is_rated = models.BooleanField(default=False)

    def __str__(self):
        return self.owner.username


class MovieRating(models.Model):
    movie = models.ForeignKey(Movie, related_name='ratedmovie', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='rateduser', on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.movie.name + self.user.username

    # @property
    # def get_two_star_percentage(self)
    #   two_star_count = MovieRating.objects.filter(rating = 2).count()
    #   total_voters = MovieRating.objects.all().count()
    #   two_star_percentage = (total_voters/two_star_count)*100
    #   return two_star_percentage

    # @property
    # def get_three_star_percentage(self)
    #   three_star_count = MovieRating.objects.filter(rating = 3).count()
    #   total_voters = MovieRating.objects.all().count()
    #   three_star_percentage = (total_voters/three_star_count)*100
    #   return three_star_percentage

    # @property
    # def get_four_star_percentage(self)
    #   one_star_count = MovieRating.objects.filter(rating = 4).count()
    #   total_voters = MovieRating.objects.all().count()
    #   one_star_percentage = (total_voters/one_star_count)*100
    #   return one_star_percentage

    # @property
    # def five_star_percentage(self)
    #   five_star_count = MovieRating.objects.filter(rating = 5).count()
    #   total_voters = MovieRating.objects.all().count()
    #   five_star_percentage = (total_voters/five_star_count)*100
    #   return five_star_percentage

    # def star_percentage(self, star_count, rating, star_percentage):
    #   total_voters = MovieRating.objects.all().count()
    #   if total_voters != 0:
    #       star_count = MovieRating.objects.filter(rating = rating).count()
    #       star_percentage = (star_count/total_voters)*100
    #       return star_percentage
    #   else:
    #       star_percentage = 0

    # @property
    # def get_one_star_percentage(self):
    #   self.star_percentage(one_star_count, 1, one_star_percentage)

    # @property
    # def get_two_star_percentage(self):
    #   self.star_percentage(two_star_count, 2, two_star_percentage)

    # @property
    # def get_three_star_percentage(self):
    #   self.star_percentage(three_star_count, 3, three_star_percentage)


    # @property
    # def four_star_percentage(self):
    #   self.star_percentage(four_star_count, 4, four_star_percentage)

    # @property
    # def five_star_percentage(self):
    #   self.star_percentage(five_star_count, 5, five_star_percentage)
