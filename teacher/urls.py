from django.urls import path
from . import views


urlpatterns = [
    path('show', views.t_show),
    path('equipmentlist', views.equipmentlist),
    path('kindjsj', views.kindjsj),
    path('kindsw', views.kindsw),
    path('kindwl', views.kindwl),
    path('kindhx', views.kindhx),
    path('kindjx', views.kindjx),
    path('kindqt', views.kindqt),
    path('stateable', views.stateable),
    path('stateunable', views.stateunable),
    path('edit', views.edit),
    path('update', views.update),
    path('addequipment', views.addequipment),
    path('save', views.save),
    path('delete', views.delete),
    path('userlist', views.userlist),
    path('deleteuser', views.deleteuser),
    path('applylist', views.applylist),
    path('yes', views.yes)
]

