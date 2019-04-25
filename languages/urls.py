from django.urls import path
from django.conf.urls import include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)

urlpatterns = [
	path('', include(router.urls))	
]