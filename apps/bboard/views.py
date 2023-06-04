from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy  # Лучше использвать этот метод для перенаправления
from .models import *
from .forms import BoardForm


class ByMainPageView(ListView):
    model = Board
    template_name = 'bboard/index.html'
    context_object_name = 'bbs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class ByRubricView(ListView):
    model = Board
    template_name = 'bboard/by_rubric.html'
    context_object_name = 'bbs'

    def get_queryset(self):
        rubric_id = self.kwargs['rubric_id']
        return Board.objects.filter(rubric=rubric_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rubric_id = self.kwargs['rubric_id']
        context['rubrics'] = Rubric.objects.all()
        context['current_rubric'] = Rubric.objects.get(pk=rubric_id)
        return context


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BoardForm
    success_url = reverse_lazy('index')  # /bboard/ дурной тон не использвать

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
