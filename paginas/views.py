from django.views.generic import TemplateView

# Referência a página que ira ser renderizada
class IndexView(TemplateView):
    template_name = "paginas/index2.html"

class SobreView(TemplateView):
    template_name = "paginas/sobre.html"
