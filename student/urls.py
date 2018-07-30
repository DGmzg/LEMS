from django.urls import path
from . import views


urlpatterns = [
    path('show', views.s_show),
    path('equipmentlist', views.equipmentlist),
    path('kindjsj', views.kindjsj),
    path('kindsw', views.kindsw),
    path('kindwl', views.kindwl),
    path('kindhx', views.kindhx),
    path('kindjx', views.kindjx),
    path('kindqt', views.kindqt),
    path('myequipment', views.myequipment),
    path('borrow', views.borrow),
    path('returnback', views.returnback),

]