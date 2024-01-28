from django.urls import path
from blog import views as blog_views
urlpatterns = [
    path('home/',blog_views.home_page_view,name='blog'),
]