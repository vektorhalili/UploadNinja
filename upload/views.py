from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View,ListView,DetailView

from .forms import *
from .models import *


# Create your views here.
class IndexView(View):
    template_name = 'upload/index.html'
    form_class = FileForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/files')
        return render(request, self.template_name, {'form' : form})


class FileListView(ListView):
    model = File

class FileDetailView(DetailView):
    model = File

class FileDownloadView(View):
    model = File
    slug = None
#class UploadView(FormView):
#    template_name = 'index.html'
#    form_class = FileForm
#    success_url = '/'
#    def form_valid(self, form):
#        return HttpResponseRedirect('/')
