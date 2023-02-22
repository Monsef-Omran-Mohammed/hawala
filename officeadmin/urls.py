from django.urls import path
from . import views

app_name = 'officeadmin'

urlpatterns = [
    path('home', views.home, name='home'),
    path('createOffice', views.createOffice, name="create-office"),
    path('officesList', views.officesList, name="offices-list"),
    path('officeList/<int:office_id>', views.office, name="office"),
    path('officeList/<int:office_id>/emailUpdate', views.officeEmailUpdate, name="office-email-update"),
    path('officeList/<int:office_id>/phoneUpdate', views.officePhoneUpdate, name="office-phone-update"),
    path('officeList/<int:office_id>/activeUpdate', views.officeActiveUpdate, name="office-active-update"),
]
