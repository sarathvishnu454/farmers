from . import views
from django.urls import path
urlpatterns=[
    path('image5',views.image5,name="image5"),
    path('table1',views.table1,name='table1'),
    path('',views.indextemplate,name='index'),
    path("register",views.register_request,name="register"),
    path("login",views.login_request,name="login"),
    path("logout",views.logout_request,name="logout")

]
