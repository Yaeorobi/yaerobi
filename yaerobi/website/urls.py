from django.urls import path


from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('GetTime', views.get_time, name='GetTime')
    ]
