from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api_rest', views.UserViewSet)

urlpatterns = [
    path('search/', views.UserSearchListView.as_view(), name='search'),
    path('', views.UserListView.as_view(), name='user_list'),

    # User CRUD
    path('create/', views.UserCreateView.as_view(), name='user_create'),
    path(
        'update/<int:id>/',
        views.UserUpdateView.as_view(),
        name='user_update'
    ),
    path(
        'delete/<int:id>/',
        views.UserDeleteView.as_view(),
        name='user_delete'
    ),
    path(
        'delete_all/',
        views.UserDeleteAll.as_view(),
        name='delete_all_users'
    ),
]

urlpatterns += router.urls
