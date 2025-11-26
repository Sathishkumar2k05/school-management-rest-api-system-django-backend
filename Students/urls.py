from django.urls import path
from .views import *

urlpatterns = [
    path('details/', StudentAPI.as_view()),
    path('details/<int:student_id>/', StudentAPI.as_view()),

    path('task/',TaskView.as_view()),
    path('task/<int:task_id>/',TaskView.as_view()),

    path('rank/',RankSheetView.as_view()),
    path('rank/<int:id>/',RankSheetView.as_view()),
]