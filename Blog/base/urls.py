from django.urls import path
from . import views




urlpatterns = [
    path('',views.getRoutes, name='routes'),
    path('blog/',views.getBlog,name='blog'),
    path('blog/<str:pk>/',views.getArtical,name='artical')

]