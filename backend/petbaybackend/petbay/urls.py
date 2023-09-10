from django.urls import path, include
from rest_framework import routers

from .views.accessories_views import AccessoriesViewSet
from .views.feed_views import FeedCreateView, FeedDeleteView, UpdateRetrieveFeedView, ListFeedView
from .views.pet_views import PetTypeListCreateView, PetListCreateView, PetRetrieveUpdateDeleteView, \
    PetTypeRetrieveUpdateDeleteView

# Create a router and register your viewsets
router = routers.DefaultRouter()
router.register(r'accessory', AccessoriesViewSet)

urlpatterns = [
    path('create_list_pet', PetListCreateView.as_view(), name='create_pet'),
    path('pets/<int:pk>', PetRetrieveUpdateDeleteView.as_view(), name='pet-retrieve-update-delete'),
    path('create_list_pettype', PetTypeListCreateView.as_view(), name='create_pettype'),
    path('pettypes/<int:pk>', PetTypeRetrieveUpdateDeleteView.as_view(), name='pettype-retrieve-update-delete'),
    path('create_feed', FeedCreateView.as_view(), name='create_feed'),
    path('delete_feed', FeedDeleteView.as_view(), name='delete_feed'),
    path('retrieve_all_feeds', ListFeedView.as_view(), name='retrieve_all_feed'),
    path('update_retrieve_feed/<int:pk>', UpdateRetrieveFeedView.as_view(), name='update_retrieve_feed'),
    path('', include(router.urls)),
]
