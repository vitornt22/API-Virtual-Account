from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

app_name = "operation"

operation_api_router = SimpleRouter()
operation_api_router.register(
    'operation/api', views.OperationApi,
    basename='operation'
)
urlpatterns = [
    path('extract/api/<int:pk>/getExtracts/<int:month>/<int:year>/',
         views.OperationApi.as_view({"get": "getExtracts"})),
]
urlpatterns += operation_api_router.urls
