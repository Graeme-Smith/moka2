from django.urls import path
from . import views
from variant_db.views import PatientListView

urlpatterns = [
    path('', views.home, name='home'),
    path('manual_import/', views.manual_import, name='manual_import'),
    #path('view/', views.view, name='view'),
    path('view/', PatientListView.as_view(), name='view')
]
