from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework_swagger.views import get_swagger_view


router = DefaultRouter()
router.register(r'row_permit_data', views.RowPermitDataViewSet)

schema_view = get_swagger_view(title='ROW Permit Data')

urlpatterns = [
    url(r'^schema/', schema_view),
    url(r'^api/', include(router.urls)),
]