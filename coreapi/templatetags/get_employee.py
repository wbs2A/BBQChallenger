from django import template
from coreapi.models import Barbeque

register = template.Library()


@register.filter(name='check_employee')
def get_employee_qs(queryset, user):
    for employee in queryset:
        if employee.user.id == user:
            return True
    return False

