from django.urls import path,include
from .import views as v
from django.contrib.auth import views as uv


urlpatterns = [
    path('', v.index, name="index"),
    path('signup/', v.signup, name="signup"),
    path('login/',uv.LoginView.as_view(template_name="authentication/login.html")),
    path('profile/', v.profile, name="profile"),
    path('logout/', uv.LogoutView.as_view(template_name="authentication/logout.html"))
    ]

