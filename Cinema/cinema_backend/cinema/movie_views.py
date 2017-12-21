from django.views.generic import ListView, CreateView, UpdateView, View, DeleteView
from .models import Movie, MovieRating
from django.contrib.auth.models import User
from django.urls import reverse_lazy
import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator


# class MovieListView(ListView):
#     today = datetime.date.today()
#     ten_days_ago = today - datetime.timedelta(days=10)
#     model = Movie
#     template_name = 'cinema/home.html'

#     def get_context_data(self, **kwargs):
#         context = super(MovieListView, self).get_context_data(**kwargs)
#         up_coming_movies = Movie.objects.filter(release_date__gt=self.today)
#         now_showing = Movie.objects.filter(release_date__range=(self.ten_days_ago, self.today))
#         context['up_coming_movies'] = up_coming_movies
#         context['now_showing_movies'] = now_showing
#         return context

# class MovieListView(ListView):
#     model = Movie
#     template_name = 'cinema/home.html'
#     paginate_by = 2
#     context_object_name = 'Movies'

class MovieListView(View):
    today = datetime.date.today()
    ten_days_ago = today - datetime.timedelta(days=10)
    template_name = 'cinema/home.html'

    def get(self, request):
        up_coming_movies = Movie.objects.filter(release_date__gt=self.today)
        now_showing = Movie.objects.filter(release_date__range=(self.ten_days_ago, self.today))
        paginator = Paginator(up_coming_movies, 2)
        page = request.GET.get('page')
        up_coming_movies = paginator.get_page(page)
        paginator = Paginator(now_showing, 2)
        page = request.GET.get('page')
        now_showing = paginator.get_page(page)
        context = {

            'up_coming_movies': up_coming_movies,
            'now_showing_movies': now_showing
        }
        return render(request, self.template_name, context)


class MovieSearchView(ListView):
    template_name = 'cinema/home.html'
    paginate_by = 2

    def get(self, request):
        name = request.GET.get('name')
        page = request.GET.get('page')
        movies = Movie.objects.all().filter(
            Q(name__icontains=name) |
            Q(genre__name__icontains=name) |
            Q(tag__tag_name__icontains=name)
        )
        paginator = Paginator(movies, 2)
        movies = paginator.get_page(page)
        return render(request, self.template_name, {'search_movies': movies})


class MovieDetailView(View):
    template_name = 'cinema/detail.html'

    def get(self, request, slug):
        movie_object = Movie.objects.get(slug=slug)
        if request.user.is_anonymous:
            return render(request, 'cinema/detail.html', {
                'Movie': movie_object,
                'error': 'You must be registered User to give rating !!!'

            })

        else:
            user_object = User.objects.get(username=self.request.user.username)
            rated_movie = user_object.rateduser.all()
            movie_filter = rated_movie.filter(movie=movie_object).exists()
            # get to return oject not queryset

            if movie_filter:
                rating = rated_movie.filter(movie=movie_object).get().rating
                context = {

                    'Movie': movie_object,
                    'rating': rating
                }
                return render(request, self.template_name, context)
            else:
                context = {

                    'Movie': movie_object
                }

                return render(request, self.template_name, context)


class MovieCreateView(CreateView):
    model = Movie
    template_name = 'cinema/create.html'
    fields = ('__all__')
    success_url = reverse_lazy('movie:movie-list')

    def get_context_data(self, **kwargs):
        context = super(MovieCreateView, self).get_context_data(**kwargs)
        context = {

            'Create': 'Create',
            'form': self.get_form(),
            'Create_Movie': 'Create New Movie',
            'Movie': 'Movie'
        }
        return context


class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'cinema/create.html'
    fields = '__all__'
    success_url = reverse_lazy('movie:movie-list')

    def get_context_data(self, **kwargs):
        context = super(MovieUpdateView, self).get_context_data(**kwargs)

        context = {

            'Update': 'Update',
            'form': self.get_form(),
            'Update_Movie': 'Update This Movie',
        }

        return context


class MovieDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy('movie:movie-list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


def rating_create(request):

    if request.method == "POST":
        slug = request.POST['slug']
        user = request.POST['user']
        rating = request.POST['rating']
        movie_object = Movie.objects.get(slug=slug)
        user_object = User.objects.get(username=user)
        rating_object = MovieRating.objects.create(
            movie=movie_object, user=user_object, rating=rating)
        rating_object.save()
        data = {

            'rating': rating
        }
        return JsonResponse(data)
