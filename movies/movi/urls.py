from django.urls import path
from . import views

app_name = 'movi'
urlpatterns = [
    path('', views.index, name= 'index' ),
    path('list', views.listing, name= 'listing' ),
    path('genre', views.genre, name= 'genre' ),
    path('vote', views.vote, name= 'vote' ),
    path('credit', views.credit, name= 'credit' ),
    # path('downloads', views.downloads, name='downloads'),
    # path('about', views.about, name='about'),
    # path('<int:pk>/',views.CollegeDetailView.as_view(),name='detail')
]
