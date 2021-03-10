from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name='about'),
    path('detail/<str:post_id>', views.post_detail, name='detail'),
    path('create_post/', views.CreatePost.as_view(), name='create_post'),
    path('detail/<slug:pk>/update/', views.EditPost.as_view(), name='edit_post'),
    path('detail/<slug:pk>/delete/', views.DeletePost.as_view(), name='delete_post'),
]