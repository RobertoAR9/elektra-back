from django.conf.urls import include
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from apps.cards import views

router = DefaultRouter()

urlpatterns = [
    re_path(r"^", include(router.urls)),
    path("card/", views.CardView.as_view()),
    path("card/<int:pk>/", views.CardDetailView.as_view()),
]

