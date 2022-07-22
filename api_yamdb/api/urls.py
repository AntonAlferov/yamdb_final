from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (APISignUp, APIToken, CategoryViewSet, CommentViewSet,
                    GenreViewSet, ReviewsViewSet, TitleViewSet, UsersViewSet)

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(
    'genres',
    GenreViewSet, basename='genres'
)
router_v1.register(
    'categories',
    CategoryViewSet, basename='categores'
)
router_v1.register(
    'titles',
    TitleViewSet, basename='titles'
)
router_v1.register(
    r'titles/(?P<title_id>\w+)/reviews',
    ReviewsViewSet, basename='review'
)
router_v1.register(
    r'titles/(?P<title_id>\w+)/reviews/(?P<review_id>\w+)/comments',
    CommentViewSet, basename='comment'
)
router_v1.register(
    'users',
    UsersViewSet,
    basename='users'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/token/', APIToken.as_view(),
         name='token_obtain_pair'),
    path('v1/auth/signup/', APISignUp.as_view(), name='signup'),
]
