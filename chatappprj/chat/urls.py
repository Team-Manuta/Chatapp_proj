from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name="home"),
    path('<str:room>/', views.room, name="room"),
    path('checkview', views.checkview, name="checkview"),
    path('send', views.send, name="send"),
    path('getMessages/<str:room>/', views.getMessages, name="getMessages"),
    path('logout/', LogoutView.as_view(next_page='home'), name="logout"),


]