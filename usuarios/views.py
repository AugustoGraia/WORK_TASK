from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
# Create your views here.


class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name="Docente")  # verificando se existe um grupo com esse nome

        url = super().form_valid(form)  

        self.object.groups.add(grupo) # adicionando o grupo o usuário ao grupo
        self.object.save() # salvando

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Usuários"
        context['button'] = "Cadastrar"
        context['icon'] = '<i class="fa-solid fa-user-check"></i>'

        return context