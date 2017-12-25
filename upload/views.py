from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View,ListView,DetailView
from django.conf import settings
from .forms import *
from .models import *
from django.http import HttpResponse

# Create your views here.
class IndexView(View):
    template_name = 'upload/index.html'
    form_class = FileForm
    def get(self, request,*args, **kwargs):
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
    def get(self, request, *args, **kwargs):
        fileslug = kwargs['slug']
        downfile = str(File.objects.get(slug=fileslug))
        file_path = os.path.join(settings.MEDIA_ROOT, downfile)
        print(file_path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                print(fh.name)
                response = HttpResponse(fh.read(), content_type="multipart/form-data")
                response['Content-Disposition'] = 'attachment; filename='+downfile
                return response
        else:
            raise Http404
