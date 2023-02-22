from django.db import models
from django.urls import reverse
from account.models import TblOfficeUser
# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CheckConstraint, Q

class TblMoneyTransfer(models.Model):
    sender_office = models.ForeignKey(TblOfficeUser, related_name='from_office', on_delete=models.CASCADE)
    recipient_office = models.ForeignKey(TblOfficeUser, related_name='to_office', on_delete=models.CASCADE)
    sent_amount = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(1000000000.0)])
    sender_commission = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(1000000.0)])
    recipient_commission = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(1000000.0)])
    commission_from_sender = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1000000.0)])
    commission_from_recipient = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1000000.0)])
    approval_by_recipient = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)
    approval_at = models.DateTimeField(null=True, blank=True)
    rejection_at = models.DateTimeField(null=True, blank=True)
    note = models.TextField(max_length=200, null=True, blank=True)
    rejection = models.BooleanField(default=False)
    note2 = models.TextField(max_length=200, null=True, blank=True)

    # الحوالة الصادرة
    def get_outgoing_money_order_url(self):
        return reverse('office:outgoing-money-order', kwargs={'money_order_id': self.pk})
    # الحوالة الواردة
    def get_incoming_money_order_url(self):
        return reverse('office:incoming-money-order', kwargs={'money_order_id': self.pk})
    # الموافقة على الحوالة
    def get_approval_incoming_money_order_url(self):
        return reverse('office:approval-incoming-money-order', kwargs={'money_order_id': self.pk})
    # رفض الحوالة
    def get_rejection_incoming_money_order_url(self):
        return reverse('office:rejection-incoming-money-order', kwargs={'money_order_id': self.pk})


class TblOfficePhone(models.Model):
    office = models.ForeignKey(TblOfficeUser, related_name='office', on_delete=models.CASCADE)
    phone = models.CharField(max_length = 14)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def get_phone_number_update_url(self):
        return reverse('office:phone-number-update', kwargs={'phone_number_id': self.pk})
    def get_phone_number_delete_url(self):
        return reverse('office:phone-number-delete', kwargs={'phone_number_id': self.pk})