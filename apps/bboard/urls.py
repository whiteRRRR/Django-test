from django.urls import path
from .views import *

urlpatterns = [
    path('', ByMainPageView.as_view(), name='index'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', ByRubricView.as_view(), name='by_rubric'),
    path('<str:type_char>/', ByTypesBoard.as_view(), name='type_board'),
]