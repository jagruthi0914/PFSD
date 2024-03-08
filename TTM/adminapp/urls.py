
from django.urls import path
from .import views

urlpatterns = [
    # path("tthome",views.h,name="ttmhome"),
    path("checkadminlogin", views.checkadminlogin, name="checkadminlogin"),
    path("checkRegistration", views.checkregistration, name="checkregistration"),
    path("checkpackages", views.checkpackages, name="checkpackages"),
]