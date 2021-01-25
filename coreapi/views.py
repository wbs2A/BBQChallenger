from django.shortcuts import render
from .models import Barbeque
# Create your views here.
def list_barbeque(request):
    bbq_list = Barbeque.objects.all()

    return render(request, 'coreapi/barbeques.html', {'list': bbq_list, 'placeholders': range(3)})

