from django.urls import path
# Importa as views que a gente criou

from .views import CampoCreate, AtividadeCreate, StatusCreate, ClasseCreate, CampusCreate, ProgressaoCreate, ComprovanteCreate
from .views import CampoUpdade, AtividadeUpdade, ProgressaoUpdate, ClasseUpdate, ComprovanteUpdate
from .views import CampoDelete, AtividadeDelete, ProgressaoDelete, ClasseDelete, ComprovanteDelete
from .views import CampoList, AtiviadeList, ClasseList, ProgressaoList, ComprovanteList

# Tem que ser urlpatterns porque é padrão do Django

urlpatterns = [
    # Todo path tem endeereço, sua_view.as_view() e nome
    # path(endereço/, nome da view.as_view(), nome= da url)
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastro-campo'),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),
    path('cadastrar/status/', StatusCreate.as_view(), name='cadastrar-status'),
    path('cadastrar/classe/', ClasseCreate.as_view(), name='cadastrar-classe'),
    path('cadastrar/campus/', CampusCreate.as_view(), name='cadastrar-campus'),
    path('cadastrar/progressao/', ProgressaoCreate.as_view(), name='cadastrar-progessao'),
    path('cadastrar/comprovante/', ComprovanteCreate.as_view(), name='cadastrar-comprovante'),
    
    
    # QUANDO FOR FAZER UM UPDATE SEGUIR ESSES PASSOS
    # <int:pk>
    path('editar/campo/<int:pk>', CampoUpdade.as_view(), name='editar-campo'),
    path('editar/atividade/<int:pk>', AtividadeUpdade.as_view(), name='editar-atividade'),
    path('editar/classe/<int:pk>/', ClasseUpdate.as_view(), name='editar-classe'),
    path('editar/progressao/<int:pk>/', ProgressaoUpdate.as_view(), name='editar-progressao'),
    path('editar/comprovante/<int:pk>/', ComprovanteUpdate.as_view(), name='editar-comprovante'),
    
    path('excluir/campo/<int:pk>', CampoDelete.as_view(), name='excluir-campo'),
    path('excluir/atividade/<int:pk>', AtividadeDelete.as_view(), name='excluir-atividade'),
    path('excluir/classe/<int:pk>/', ClasseDelete.as_view(), name='excluir-classe'),
    path('excluir/progressao/<int:pk>/', ProgressaoDelete.as_view(), name="excluir-progressao"),
    path('excluir/comprovante/<int:pk>/', ComprovanteDelete.as_view(), name="excluir-comprovante"),


    path('listar/campos/', CampoList.as_view(), name='listar-campos'),
    path('listar/atividades/',AtiviadeList.as_view(), name='listar-atividades'),
    path('listar/classes/', ClasseList.as_view(), name='listar-classe'),
    path('listar/progressoes/', ProgressaoList.as_view(), name="listar-progressao"),
    path('listar/comprovante/', ComprovanteList.as_view(), name='listar-comprovante'),

]
