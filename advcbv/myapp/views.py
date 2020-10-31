from myapp import models
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView,TemplateView,ListView,DetailView
# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["injectme"] = "hehehe injected"
        return context
    

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name',"principal",'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("list")