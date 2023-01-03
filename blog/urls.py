from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'), #deleted the .as_view() part
    path("about", views.AboutPageView.as_view(), name="about")
]
