from django.urls import path
from .movie_views import (
    MovieListView,
    MovieCreateView,
    MovieDetailView,
    MovieUpdateView,
    MovieSearchView,
    MovieDeleteView,
    rating_create
)

from .user_views import (
    UserRegisterView,
    UserProfileView,
    UserUpdateView,
    PasswordChangeView
)

from .genre_views import (
    GenreCreateView,
    GenreListView,
    GenreDeleteView
)

from .tag_views import (
    TagCreateView,
    TagListView,
    TagDeleteView,
    TagUpdateView
)

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test

admin_or_none = user_passes_test(lambda u: u.is_anonymous or u.is_staff)

app_name = 'movie'

urlpatterns = [

    path('', MovieListView.as_view(), name='movie-list'),
    path('search/', MovieSearchView.as_view(), name='movie_search'),
    path('create/', staff_member_required(MovieCreateView.as_view()), name='movie-create'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie-detail'),
    path('<slug:slug>/update', staff_member_required(
        MovieUpdateView.as_view()), name='movie-update'),
    path('<int:pk>/delete', staff_member_required(MovieDeleteView.as_view()), name='movie-delete'),


    path('genre/create/', staff_member_required(GenreCreateView.as_view()), name='genre_create'),
    path('genre/list/', staff_member_required(GenreListView.as_view()), name='genre_list'),
    path('genre/<int:pk>/delete', staff_member_required(
        GenreDeleteView.as_view()), name='genre_delete'),



    path('tag/create', staff_member_required(TagCreateView.as_view()), name='tag_create'),
    path('tag/list', staff_member_required(TagListView.as_view()), name='tag_list'),
    path('tag/<int:pk>/update', staff_member_required(TagUpdateView.as_view()), name='tag_update'),
    path('tag/<int:pk>/delete', staff_member_required(TagDeleteView.as_view()), name='tag_delete'),


    path('user/register/', admin_or_none(UserRegisterView.as_view()), name='user_register'),
    path('user/profile/', login_required(UserProfileView.as_view()), name='user_detail'),
    path('user/update/', login_required(UserUpdateView.as_view()), name='user_update'),
    path('user/profile/change_password/', login_required(
        PasswordChangeView.as_view()), name='change_password'),
    path('user/login/', admin_or_none(
        LoginView.as_view(template_name='user/login.html')), name='login'),
    path('user/logout/', login_required(LogoutView.as_view(next_page='/movie/')), name='logout'),

    # path('rating/<slug:slug>/<str:user>/<str:movie>/<int:rating>/', rating_create,  name='movie_rating')

    path('rating/create/', rating_create, name='movie_rating')

]
