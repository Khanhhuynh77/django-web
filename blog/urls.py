from django.urls import path
from . import views

from django.http import Http404
urlpatterns = [
  path('', views.PostListView.as_view(), name='blog'),
  path('<int:pk>/', views.post, name='post'),

]

"""  
path('', views.list),
  path('<int:id>/', views.post),
  """