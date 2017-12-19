from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from cinema.models import Tag
from django.urls import reverse_lazy


class TagCreateView(CreateView):
    model = Tag
    template_name = 'tag/create.html'
    fields = ('movie', 'tag_name')
    success_url = reverse_lazy('movie:tag_list')

    def get_context_data(self, **kwargs):
        context = super(TagCreateView, self).get_context_data(**kwargs)
        context = {

            'Create' : 'Create',
            'Topic' : 'Create Movie Tags Here !!!',
            'form' : self.get_form()
        }
        return context


class TagListView(ListView):
    model = Tag
    template_name = 'tag/create.html'
    context_object_name = 'Tags'

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        context['List'] = 'These are the tags associated with respective Movies'
        return context


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy('movie:tag_list')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class TagUpdateView(UpdateView):
    model = Tag
    template_name = 'tag/create.html'
    fields = '__all__'
    success_url = reverse_lazy('movie:tag_list')

    def get_context_data(self, **kwargs):
        context = super(TagUpdateView, self).get_context_data(**kwargs)
        context = {

            'Update': 'Update',
            'Topic': 'Update Your Movie Tags Here !!!',
            'form': self.get_form()
        }
        return context
