from django.urls import path
from .views import (
   PostsList, PostDetail, NewsCreate, PostUpdate, PostDelete, NewsSearch,
   subscriptions
)
from django.views.decorators.cache import cache_page


urlpatterns = [
   path('', cache_page(60)(PostsList.as_view()), name='post_list'),
   path('<int:pk>', cache_page(300)(PostDetail.as_view()), name='post_detail'),
   path('search/', NewsSearch.as_view(), name='post_search'),
   path('create/', NewsCreate.as_view(), name='news_create'),
   path('articles/create/', NewsCreate.as_view(), name='news/articles_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('subscriptions/', subscriptions, name='subscriptions'),

]
