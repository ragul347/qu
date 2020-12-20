from django.contrib import admin
from django.urls import path,include
from quizz import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('quiz/',include('quizz.urls')),
    path('logout/',views.user_logout,name="logout"),
    path('special/',views.special,name='special'),
    path('login/',views.user_login,name='user_login'),
    path('register/',views.register,name='register'),
]
