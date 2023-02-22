from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'office'

urlpatterns = [
    path('officeList', views.officeList, name="office-list"),
    path('officeList/<int:office_id>', views.office, name="office-user"),
    path('officeProfile', views.officeProfile, name="office-profile"),
    path('officeProfile/officeProfileUpdate', views.officeProfileUpdate, name="office-profile-update"),
    path("officeProfile/changeOfficePassword", views.ChangeOfficePassword.as_view(), name="change-office-password"),
    path('officeProfile/createOfficePhoneNumber', views.createOfficePhoneNumber, name="create-office-phone-number"),
    path('officeProfile/<int:phone_number_id>/update', views.phoneNumberUpdate, name="phone-number-update"),
    path('officeProfile/<int:phone_number_id>/delete', views.phoneNumberDelete, name="phone-number-delete"),
    # ==========
    path('outgoingTransfersList', views.outgoingTransfersList, name="outgoing-transfers-list"),
    path('doneOutgoingTransfersList', views.doneOutgoingTransfersList, name="done-outgoing-transfers-list"),
    path('waitingOutgoingTransfersList', views.waitingOutgoingTransfersList, name="waiting-outgoing-transfers-list"),
    path('rejectedOutgoingTransfersList', views.rejectedOutgoingTransfersList, name="rejected-outgoing-transfers-list"),
    path('outgoingMoneyOrder/<int:money_order_id>', views.outgoingMoneyOrder, name='outgoing-money-order'),
    # ==========
    path('incomingTransfersList', views.incomingTransfersList, name="incoming-transfers-list"),
    path('doneIncomingTransfersList', views.doneIncomingTransfersList, name="done-incoming-transfers-list"),
    path('waitingIncomingTransfersList', views.waitingIncomingTransfersList, name="waiting-incoming-transfers-list"),
    path('rejectedIncomingTransfersList', views.rejectedIncomingTransfersList, name="rejected-incoming-transfers-list"),
    path('incomingMoneyOrder/<int:money_order_id>', views.incomingMoneyOrder, name='incoming-money-order'),
    path('incomingMoneyOrder/<int:money_order_id>/approval', views.approvalMoneyTransfer, name='approval-incoming-money-order'),
    path('incomingMoneyOrder/<int:money_order_id>/rejection', views.rejectionMoneyTransfer, name='rejection-incoming-money-order'),
    # ==========
    path('officeStatistics', views.officeStatistics, name="office-statistics"),
]

