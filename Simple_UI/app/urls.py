"""Este modulo se encarga de generar dinamicamente los paths correspondientes
    para desplegarlos en los endpoints
"""
from rest_framework import routers
from app import views

app_name = 'app'
router = routers.DefaultRouter()

router.register('users', views.UserViewSet, basename='users')

urlpatterns = router.urls
