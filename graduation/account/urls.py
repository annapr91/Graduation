from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('child/', registchildren, name='child'),
path('login/', LoginUser.as_view(), name='login'),
path('mydata/', mydata, name='mydata'),
# path('namechange/', name_change, name= 'namechange'),

path('mydata/password_change/', PasswordsChange.as_view(template_name='password_change.html'), name='password_change'),
path('password_complete/', success_password, name='password_complete'),
path("password_reset", password_reset_request, name="password_reset"),
path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),
# path('password-change/', password_change, name='password_change'),
# path('password-change/done/', password_change_done, name='password_change_done'),


]