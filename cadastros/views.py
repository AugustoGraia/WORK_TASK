from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView # Method
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin  # Encerrar sessão 
from braces.views import GroupRequiredMixin

import usuarios # Grupos de usuários de altorização de alteração

# Uma exibição que exibe um formulário para criar um objeto, exibindo novamente o formulário com erros de validação (se houver) e salvando o objeto.


# views.py: Arquivo responsável por definir as regras de negócio do app.

from .models import Campo, Atividade, Status, Classe, Campus, Progressao, Comprovante, Validacao

from django.urls import reverse_lazy # Redireciona para uma página
                                     # Uma classe que cria um formulario para fazer registros no banco
class CampoCreate(GroupRequiredMixin ,LoginRequiredMixin ,CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')

    def get_context_data(self, *args, **kwargs):  # Para a definição do nome do tilulo que vc está (foi usado o     ['titulo'] no form.html)
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Campo"
        context['button'] = "Cadastrar"
        context['icon'] = '<i class="fa-solid fa-check-double"></i>'
        return context

class AtividadeCreate(GroupRequiredMixin ,LoginRequiredMixin ,CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):  
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Atividades"
        context['button'] = "Cadastrar"
        context['icon'] = '<i class="fa-solid fa-check-double"></i>'
        return context

class StatusCreate(GroupRequiredMixin ,LoginRequiredMixin ,CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Status
    fields =  ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class ClasseCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Classe
    fields = ['nome', 'nivel', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-classe')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Classe"
        context['button'] = "Cadastrar"
        context['icon'] = '<i class="fa-solid fa-check-double"></i>'
        return context

class CampusCreate(GroupRequiredMixin, LoginRequiredMixin ,CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Campus
    fields =  ['cidade', 'endereco', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class ProgressaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Progressao
    fields = ['classe', 'data_inicial', 'data_final', 'observacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-progressao')

    def form_valid(self, form): # Função para mostrar qual usuário cadastrol
    
        # Validando que o usuario é igual request.User
        form.instance.usuario = self.request.user
        # Criando o objeto com os dados do usuario
        url = super().form_valid(form)
        # Aterando o objeto 
        # self.object.observacao += " [TESTE]"
        # self.object.save()
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastrar progessao'
        context['button'] = 'Cadastrar'
        context['icon'] = '<i class="fa-solid fa-check-double"></i>'
        return context

class ComprovanteCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Comprovante
    fields = ['progressao', 'atividade', 'quantidade', 'data', 'data_final', 'arquivo']
    template_name = 'cadastros/form-upload.html'
    success_url = reverse_lazy('listar-comprovante')

    def form_valid(self, form):  
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['button'] = 'Cadastrar'
        context['icon'] = '<i class="fa-solid fa-check-double"></i>'
        return context

########## UPDATE ##########

 # Uma exibição que exibe um formulário para editar um objeto existente, exibindo novamente o formulário com erros de validação (se houver) e salvando as alterações no objeto. Isso usa um formulário gerado automaticamente da classe de modelo do objeto (a menos que uma classe de formulário seja especificada manualmente)

class CampoUpdade(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Campo
    fields = ["nome", "descricao"]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')

    def get_context_data(self, *args, **kwargs): 
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Campo"
        context['button'] = "Salvar"
        context['icon'] = '<i class="fa-solid fa-check-double"></i>'
        return context

class AtividadeUpdade(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')
    
    def get_context_data(self, *args, **kwargs):  
        context = super().get_context_data(*args, **kwargs)
        context['button'] = "Salvar"
        context['titulo'] = "Alterar Atividade"
        context['icon'] = '<i class="fa-solid fa-check-double"></i>'
        return context

class ProgressaoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Progressao
    fields = ['classe', 'data_inicial', 'data_final', 'observacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-progressao')

    def get_object(self, queryset=None): # Faz a referência para somento o usuário que criou a a progreção possa ter asseco a ela e editar pelo ID
        self.object = get_object_or_404(Progressao, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Editar Progressão'
        context['button'] =  'Salvar'
        context['icon'] = '<i class="fa-solid fa-check-double"></i>'
        return context

class ClasseUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Classe
    fields = ['nome', 'nivel', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-classe')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Alterar Classe"
        context['button'] = "Salvar"
        context['icon'] = '<i class="fa-solid fa-check-double"></i>'
        return context

class ComprovanteUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Comprovante
    fields = ['progressao', 'atividade', 'quantidade', 'data', 'data_final', 'arquivo']
    template_name = 'cadastros/form-upload.html'
    success_url = reverse_lazy('listar-comprovante')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Comprovante, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['button'] = 'Salvar'
        context['icon'] = '<i class="fa-solid fa-check-double"></i>'
        return context
    
########## DELETE ##########

class CampoDelete(GroupRequiredMixin ,LoginRequiredMixin ,DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campos')

class AtividadeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')   
    group_required = u"Administrador" 
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campos')

class ClasseDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Classe
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-classe')

class ProgressaoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador" 
    model = Progressao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-progressao')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Progressao, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

class ComprovanteDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Comprovante
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-comprovante')

    def get_object(self, queryset=None): # Método para que só o usuário que queriou o comprovante possa excluir
        self.object = get_object_or_404(Comprovante, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

########## LIST ##########

class CampoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Campo
    template_name = 'cadastros/listas/campo.html'
    

class AtiviadeList(LoginRequiredMixin ,ListView):
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/listas/atividade.html'

class ClasseList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Classe
    template_name = 'cadastros/listas/classe.html'

class ProgressaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Progressao
    template_name = 'cadastros/listas/progressao.html'

    def get_queryset(self):  # Função para que somente o usuário que cadastrou veja essa lista
        self.object_list = Progressao.objects.filter(usuario=self.request.user)
        return self.object_list

class ComprovanteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Comprovante
    template_name = 'cadastros/listas/comprovante.html'
