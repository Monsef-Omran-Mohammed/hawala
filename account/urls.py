from django.urls import path
from . import views
app_name = 'account'

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name="logout"),

    path('officeRegister/', views.office_register, name='office-register'),
    path('officeUsers/', views.office_users, name='office-users'),

    path('officeUsers/<int:pk>', views.office_user_page, name='office-user-page'),
    path('officeUsers/<int:pk>/update', views.office_user_update, name='office-user-update'),
]
