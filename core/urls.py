from django.urls import path
from .views import index, sobrenos, sobre

urlpatterns = [
    path('', index, name='index'),
    path('sobrenos/', sobrenos, name='sobrenos'),
    path('sobre/', sobre, name='sobre'),
]
