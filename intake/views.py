from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Case
from django.template import loader
from django.urls import reverse
from django.views import generic
from . import forms

# Create your views here.


# def index(request):
#     latest_entry_list = Case.objects.order_by('-entry_date')[:5]
#     template = loader.get_template('intake/index.html')
#     context = {
#         'latest_entry_list': latest_entry_list,
#     }
#     output = ', '.join([q.__str__() for q in latest_entry_list])
#     response = "Well, hello there!"
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'intake/index.html', context)

class IndexView(generic.ListView):
    template_name = 'intake/index.html'
    context_object_name = 'latest_entry_list'

    def get_queryset(self):
        return Case.objects.order_by('-entry_date')


# def detail(request, case_id):
#     case = get_object_or_404(Case, pk=case_id)
#     context = {
#         'case': case,
#     }
#     return render(request, 'intake/detail.html', context)

class DetailView(generic.DetailView):
    model = Case
    template_name = 'intake/detail.html'


class CaseCreate(generic.UpdateView):
    model = Case
    fields = ['your_name', 'childs_name']


def intakes(request, case_id):
    response = "intakes for %s."
    return HttpResponse(response % case_id)


def name(request):
    if request.method == 'POST':
        form = forms.NewForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = forms.NewForm()
    return render(request, 'intake/name.html', {'form': form})
