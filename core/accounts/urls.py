from django.urls import path
from .views import UserProfileView, AddFollower, RemoveFollower, ListFollower

app_name = 'accounts'

urlpatterns = [
    path('<username>/',UserProfileView.as_view(),name='profile'),
    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),
    path('profile/<int:pk>/followers',ListFollower.as_view(), name='list-follower')
]