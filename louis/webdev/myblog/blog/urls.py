from django.urls import path

from . import views

from .views import IndexView, PostView

app_name = 'blog'

urlpatterns = [
    path('<int:pk>/', IndexView.as_view(), name='index'),
    path('post/<int:post_id>/', PostView.as_view(), name='post-list'),
]