from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.cybervision, name="cybervision"),
    path('signup/',views.signup, name="signup"),
    path('signin/',views.signin, name="signin"),
    path('afterlogin/',views.afterlogin, name="afterlogin"),
    path('dataset/',views.dataset, name="dataset"),
]

# handler404 = 'myapp.views.error_404'