from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home-page'),
    path('graph',views.graph,name='josaa-graph'),
    path('plot',views.plotgraph,name='plot-graph'),
    path('selectInstitute',views.selectInstitute,name='selectInstitute'),
    path('selectBranch',views.selectBranch,name='selectBranch'),
    path('instidetails',views.InstituteDetails,name='InstituteDetails'),
]