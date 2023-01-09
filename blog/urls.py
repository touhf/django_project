from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'), #deleted the .as_view() part
    path("about", views.AboutPageView.as_view(), name="about"),
    path('upload/', views.image_upload_view),
]

urlpatterns += staticfiles_urlpatterns()
