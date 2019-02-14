from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    # path('temp/', views.temp, name = 'temp')
    # path('post_new/', views.input_post, name='post_new'),
    path('<int:post_id>/', views.cat_detail, name = 'cat_detail'),
]