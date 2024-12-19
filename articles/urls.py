from django.urls import path
from . import views

urlpatterns = [
    path("", views.ArticleListAPIView.as_view()),
    path("<int:pk>/", views.ArticleDetailAPIView.as_view()),
    path("<int:article_pk>/comments/", views.CommentListAPIView.as_view()),
    path("comments/<int:comment_pk>/", views.CommentDetailAPIView.as_view()),
]