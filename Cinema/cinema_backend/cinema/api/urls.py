from django.urls import path, include
from .views import MovieViewSet, GenreViewSet
from rest_framework.routers import DefaultRouter


router  = DefaultRouter()
router.register(r'genres', GenreViewSet)
router.register(r'movies', MovieViewSet)


urlpatterns = [

	path('', include(router.urls)),
	path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]