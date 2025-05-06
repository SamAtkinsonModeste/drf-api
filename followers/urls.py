from django.urls import path
from followers import views

urlpatterns = [
    path("", views.FollowerList.as_view()),
    path("followers/<int:pk>/", views.FollowerDetail.as_view()),
]
