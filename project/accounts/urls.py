from django.conf.urls import url
from project.accounts import views


urlpatterns = [

    url(r'^login/$', views.LoginView.as_view(), name="login"),
    url(r'^register/$', views.UserRegistrationView.as_view(), name="register"),
    url(r'^reset-password/$', view=views.PasswordResetView.as_view(), name="reset-password"),
    url(r'^user/profile/$', views.UserProfileView.as_view(), name="profile"),

]
