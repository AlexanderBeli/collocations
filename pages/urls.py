from django.urls import path
from .views import MainPageView, SearchPageView, SearchResult

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('search/', SearchPageView.as_view(), name='search'),
    path('search/result/', SearchResult.as_view(), name='result'),
]