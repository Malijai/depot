from django.urls import path
from . import views
from .views import dossier_new, pardossier


urlpatterns = [
#    url(r'^doclist/$', doclist, name='doclist'),
    path('dossierslist/', dossier_new, name='dossierslist'),
    path('dossiers/<int:pid>/', pardossier , name='dossierfolder'),
    path('<int:pid>/dossier/new/', views.dossier_new, name='dossier_new'),
]

