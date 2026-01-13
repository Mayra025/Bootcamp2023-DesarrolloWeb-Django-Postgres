from . import views
from django.urls import path

urlpatterns=[  #patrones de urls , rutas de la app
    path('',views.home, name='home'),
    path('signup/', views.do_signup, name='registro_usuario'),
    path('login/', views.do_login, name='inicio_sesion'),
    path('logout/', views.do_logout, name='cerrar_sesion')


]