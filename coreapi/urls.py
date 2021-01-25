from django.urls import path, include
from .views import list_barbeque, cancel_registr, confirm_registr, do_confirm_registr, do_cancel_employee, do_cancel_guest, detail_barbeque

urlpatterns = [
    path('', list_barbeque, name='list_bbq'),
    path('churrasco/<int:id>', detail_barbeque, name='detail_bbq'),
    path('confirm', confirm_registr, name='confirm_register'),
    path('api/confirm', do_confirm_registr, name='do_confirm'),
    path('cancel', cancel_registr, name='cancel_register'),
    path('api/cancel_guest', do_cancel_guest, name='do_cancel_guest'),
    path('api/cancel_employee', do_cancel_employee, name='do_cancel_employee')

]

