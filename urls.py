from django.urls import path
from . import views
from .views import dossier_new, pardossier

urlpatterns = [
#    url(r'^doclist/$', doclist, name='doclist'),
    path('dossiers/<int:pid>/', pardossier , name='dossier'),
    path('<int:pid>/dossier/new/', views.dossier_new, name='dossier_new'),
]

