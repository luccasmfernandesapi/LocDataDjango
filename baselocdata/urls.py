from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from apps.consultacpf import views
from apps.ticketmaster import views as view_master

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(
        next_page="/login/"
    ),
        name="logout"
    ),

    path('login/',
         auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('listardados/', views.listardados, name="listardados"),
    path('consultacpf/', views.dadosconsulta, name="consultacpf"),

    # TicketMaster
    path('ticketmaster/home/',
         view_master.home, name="hometm")

]
