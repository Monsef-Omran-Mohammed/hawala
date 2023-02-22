from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# Create your models here.

is_admin = 0
is_office = 1

USER_TYPE = (
    ('', '-------'),
    (is_admin, 'is_admin'),
    (is_office, 'is_office')
)

# User
class TblUser(AbstractUser):
    user_type = models.PositiveIntegerField(choices=USER_TYPE)

    def get_office_user_url(self):
        return reverse('account:office-user-page', kwargs={'pk': self.pk})
    def admin_get_office_email_update_url(self):
        return reverse('officeadmin:office-email-update', kwargs={'office_id': self.pk})
    def admin_get_office_active_url(self):
        return reverse('officeadmin:office-active-update', kwargs={'office_id': self.pk})
    

CITY_CHOICES = (
    ('', '-------'),
    (1, 'البيضاء'),
    (2, 'بنغازي')
)

# Office User
class TblOfficeUser(models.Model):
    user = models.OneToOneField(TblUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=1500, null=True, blank=True)
    email = models.EmailField()
    special_phone = models.CharField(max_length=14)
    city = models.PositiveIntegerField(choices=CITY_CHOICES, default=1)
    address = models.CharField(max_length=100)
    url_address = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.user}'
    
    def get_office_user_url(self):
        return reverse('office:office-user', kwargs={'office_id': self.pk})

    def get_office_user_update_url(self):
        return reverse('account:office-user-update', kwargs={'office_id': self.pk})
    
    def admin_get_office_user_url(self):
        return reverse('officeadmin:office', kwargs={'office_id': self.pk})
    def admin_get_office_phone_update_url(self):
        return reverse('officeadmin:office-phone-update', kwargs={'office_id': self.pk})


