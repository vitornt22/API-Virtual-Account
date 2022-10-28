from rest_framework.routers import SimpleRouter

from . import views

app_name = "account"

account_api_router = SimpleRouter()
account_api_router.register(
    'account/api', views.AccountApi,
    basename='account'
)
urlpatterns = account_api_router.urls
