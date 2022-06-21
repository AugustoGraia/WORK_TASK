from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Perfil

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
        Perfil.objects.create(usuario=self.object)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Usuários"
        context['button'] = "Cadastrar"
        context['icon'] = '<i class="fa-solid fa-user-check"></i>'

        return context

class PerfilUpdate(UpdateView):
    template_name = "cadastros/form.html"
    model = Perfil
    fields = ["nome_completo", "cpf", "telefone"]
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):   # Criando o objeto e veridicando qual usuário ira fazer a alteração
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object 

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Usuário"
        context['button'] = "Atualizar"

        return context






