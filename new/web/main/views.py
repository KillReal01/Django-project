from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import *
from .forms import *

security = {'Охранник': {}}
programer = {'Front-end программист': {}, 'Back-end программист': {}, 'Аналитик данных': {}}
manager = {'Менеджер': {}}
main = {'Главный менеджер': manager, 'Главный программист': programer, 'Главный охранник': security}
company = {'Директор компании': main}


def index(request):
    data_output = []

    def get_data(data_dict, data):
        for key, value in data_dict.items():
            data.append(key)
            list = [str(item) for item in Employee.objects.filter(post=key)]
            data.append(list)

            if (len(list) > 0):
                list.append([])
                get_data(value, list[-1])
            else:
                get_data(value, list)

    get_data(company, data_output)
    return render(request, 'main/index.html', {'employee': data_output})


def list(request):
    emp = {'employee': Employee.objects.all()}
    return render(request, 'main/list.html', emp)


def sort(request, sort_slug):
    if sort_slug == 'surname':
        sorted = Employee.objects.order_by('surname', 'name', 'patronymic')
    else:
        sorted = Employee.objects.order_by(sort_slug)

    emp = {'employee': sorted, 'slug': sort_slug}
    return render(request, 'main/list.html', emp)


class Registration(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('private')
    template_name = 'main/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('private')


class Login(LoginView):
    form_class = LoginForm
    template_name = 'main/verify.html'

    def get_success_url(self):
        return reverse_lazy('private')


def logout_user(request):
    logout(request)
    return redirect('verify')


def private(request):
    return render(request, 'main/private.html')
