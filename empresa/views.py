from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView

from ganancias.models import Empresa


# ------------- EMPRESAS ------------------------------------------------
class EmpresaListView(LoginRequiredMixin, ListView):
    model = Empresa
    template_name = 'ganancias/empresa/list.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Empresa.objects.filter(user=self.request.user):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_queryset(self):
        return Empresa.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Empresas'
        context['create_url'] = reverse_lazy('export_lsd:empresa_create')
        context['list_url'] = reverse_lazy('export_lsd:empresa_list')
        context['entity'] = 'Empresas'
        return context
