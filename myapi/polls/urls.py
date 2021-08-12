from django.urls import path
from . import views


urlpatterns = [
    path('mywork/', views.MyWorkView.as_view()),
    path('mywork/<int:pk>', views.MyWorkDetailView.as_view()),

    ]
