from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers

import main.settings as settings
from core.views import FilterViewList, ImagePostGeneric

router = routers.DefaultRouter()

urlpatterns = [
    path(settings.PATH_URL+'/admin/', admin.site.urls),

    # Open API 3
    path(settings.PATH_URL+'/api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(settings.PATH_URL+'/api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path(settings.PATH_URL+'/api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    #Image
    path(settings.PATH_URL+'/image/', ImagePostGeneric.as_view()),

    #Filter
    path(settings.PATH_URL+'/filter/', FilterViewList.as_view()),

]