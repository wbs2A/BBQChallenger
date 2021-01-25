from django.shortcuts import render, redirect
from .models import Barbeque, Employee


# Create your views here.

def list_barbeque(request):
    bbq_list = Barbeque.objects.all()
    return render(request, 'coreapi/barbeques.html', {'list': bbq_list, 'placeholders': range(3)})


def detail_barbeque(request, id):
    bbq = Barbeque.objects.get(pk=id)
    context = {"comida": bbq.getFoodAmount(), "bebida": bbq.getDrinkAmount(), "total": bbq.totalAmount(), "convidados": bbq.getGuests(), "participantes": bbq.getParticipants()}
    return render(request, 'coreapi/barbeque_detail.html', context)


def cancel_registr(request):
    bbq = Barbeque.objects.get(pk=request.POST.get("bbq"))
    return render(request, 'coreapi/cancel_form.html', {'bbq': bbq.id})


def do_cancel_employee(request):
    bbq = Barbeque.objects.get(pk=request.POST.get('bbq'))
    employee = Employee.objects.filter(user__exact=request.user).last()
    bbq.participants.remove(employee)
    return redirect('/')


def do_cancel_guest(request):
    employee = Employee.objects.filter(user__exact=request.user).last()
    employee.guest = False
    employee.guest_drink = False
    employee.save()
    return redirect('/')


def confirm_registr(request):
    bbq = Barbeque.objects.get(pk=request.POST.get("bbq"))
    return render(request, 'coreapi/confirm_participation.html', {'bbq': bbq.id})


def do_confirm_registr(request):
    bbq = Barbeque.objects.get(pk=request.POST.get("bbq"))
    e_drink = True if request.POST.get('employee_drinks') == 'on' else False
    h_guest = True if request.POST.get('have_guest') == 'on' else False
    g_drink = True if request.POST.get('guest_drinks') == 'on' else False

    employee = Employee.objects.create(user=request.user, drinks=e_drink, guest=h_guest, guest_drink=g_drink)
    print(employee)
    employee.save()
    bbq.participants.add(employee)
    return redirect('/')
