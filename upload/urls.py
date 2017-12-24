#from django.conf.urls import urls
from django.urls import path
from upload.views import *

app_name = 'upload'

urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('filelist/', FileListView.as_view(), name = 'FileListView'),
]
