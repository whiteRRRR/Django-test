from django.urls import path
from .views import *

urlpatterns = [
    path('', ByMainPageView.as_view(), name='index'),
    path('<int:rubric_id>/', ByRubricView.as_view(), name='by_rubric'),
    path('add/', BbCreateView.as_view(), name='add')
]