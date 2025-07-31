from django.urls import path
from .views import home, login_view, logout_view

urlpatterns = [
    path('', login_view, name='login'),
    path('home/', home, name='home'),
    path('logout/', logout_view, name='logout'),

]
