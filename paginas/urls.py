from django.urls import path
# Importa as views que a gente criou

from .views import IndexView, SobreView
# Tem que ser urlpatterns porque é padrão do Django

urlpatterns = [
    # Todo path tem endeereço, sua_view.as_view() e nome
    # path(endereço/, nome da view.as_view(), nome= da url)
    path('', IndexView.as_view(), name= 'index'),
    path('sobre/', SobreView.as_view(), name= 'sobre'),
]