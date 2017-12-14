from django.views.generic import ListView, DetailView, CreateView, UpdateView, View, DeleteView
from .models import Genre
from django.urls import reverse_lazy
from django.shortcuts import render

class GenreCreateView(CreateView):
	model = Genre
	template_name = 'genre/create.html'
	fields = ('name', )
	success_url = reverse_lazy('movie:genre_list')

	def get_context_data(self, **kwargs):
	    context = super(GenreCreateView, self).get_context_data(**kwargs)
	    context = {
	    	'Create' : 'Create',
	    	'form'  : self.get_form()

	    }

	    return context

class GenreListView(ListView):
	model = Genre
	template_name = 'genre/create.html'
	context_object_name = 'Genres'

	def get_context_data(self, **kwargs):
	    context = super(GenreListView, self).get_context_data(**kwargs)
	    context['List'] = 'These are the available genres'
	    return context

class GenreDeleteView(DeleteView):
	model = Genre
	success_url = reverse_lazy('movie:genre_list')