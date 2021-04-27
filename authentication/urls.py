from django.urls import path,include
from .import views as v
from django.contrib.auth import views as uv


urlpatterns = [
    path('', v.index, name="home"),
    path('signup/', v.signup, name="signup"),
    path('login/',uv.LoginView.as_view(template_name="authentication/login.html"), name='login'),
    path('profile/', v.profile, name="profile"),
    path('logout/', uv.LogoutView.as_view(template_name="authentication/logout.html"), name='logout'),
    path('password_reset/', uv.PasswordResetView.as_view(template_name="authentication/password_reset.html"), name='pass_reset'),
    path('password_reset/done/', uv.PasswordResetDoneView.as_view(template_name="authentication/password_reset_done.html"), name='pass_reset_done'),
    path('reset/<uidb64>/<token>/', uv.PasswordResetConfirmView.as_view(template_name="authentication/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', uv.PasswordResetCompleteView.as_view(template_name="authentication/password_reset_complete.html"), name='pass_reset_complete'),
   
    ]

