from django.urls import path,include
from . import views as v

urlpatterns = [
    path('', v.index, name="index"),
    path('signup/', v.signup, name="signup"),]

