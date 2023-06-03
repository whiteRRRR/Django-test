from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy  # Лучше использвать этот метод для перенаправления
from .models import *
from .forms import BoardForm


def index(request):
    bbs = Board.objects.all()
    rubrics = Rubric.objects.all()
    contex = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/templates/bboard/index.html', contex)


def by_rubric(request, rubric_id):
    bbs = Board.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics,
               'current_rubric': current_rubric}
    return render(request, 'bboard/templates/bboard/by_rubric.html', context)


class BbCreateView(CreateView):
    template_name = 'bboard/templates/bboard/create.html'
    form_class = BoardForm
    success_url = reverse_lazy('index')  # /bboard/ дурной тон не использвать

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
