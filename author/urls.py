from django.urls import path
from .import views
urlpatterns = [
    path('register/',views.register, name='register'),
    path('login/',views.loginForm,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name="profile"),
    path('profile_update/',views.profileUpdate, name='profile_update'),
    path('password_change/',views.change_password, name='password_change'),
    path('new_blog/',views.new_blog,name='new_blog'),
    path('delete_post/<int:pk>/',views.delete_post,name="delete_post"),
    path('edit_post/<int:pk>/',views.edit_post,name="edit_post"),
    path('blogs/',views.all_blog,name='all_blog'),
]
 