#from django.conf.urls import urls
from django.urls import path, re_path
from upload.views import *

app_name = 'upload'

urlpatterns = [
    path('', IndexView.as_view(), name = 'index'),
    path('files/', FileListView.as_view(), name = 'FileListView'),
    path('file/<slug:slug>/', FileDetailView.as_view(), name = 'FileDetailView'),
    path('file/<slug:slug>/download', FileDownloadView.as_view(), name = 'FileDownloadView'),
]
