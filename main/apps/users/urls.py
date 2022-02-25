from django.urls import path
from .views import UsersSignUpView

app_name = 'users'
urlpatterns = [
    path('users_signup/', UsersSignUpView.as_view() ,name='users_signup'),
]
