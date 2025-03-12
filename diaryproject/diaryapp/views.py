from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from . models import Entry
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.
def home(request):
    return render(request, 'diaryapp/home.html')


class EntryListView(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("-date_created")
    context_object_name = 'entry_list'
    template_name = 'diaryapp/entry_list.html'


class EntryDetailView(DetailView):
    model = Entry


class EntryCreateView(SuccessMessageMixin, CreateView):
    model = Entry
    fields = ['title', 'content']
    template_name = "diaryapp/entry_form.html"
    success_url = reverse_lazy("entry-list")
    success_message = "Your new entry was created!"


class EntryUpdateView(SuccessMessageMixin, UpdateView):
    model = Entry
    fields = ["title", "content"]
    success_message = "Your entry was updated!"

    def get_success_url(self):
        return reverse_lazy("entry-detail", kwargs={"pk": self.object.pk})


class EntryDeleteView(SuccessMessageMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")
    success_message = "Your entry was deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
