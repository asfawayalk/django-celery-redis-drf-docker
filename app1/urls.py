from django.urls import include, re_path as url
from rest_framework.routers import DefaultRouter
from .views import ItemsViewset, CreateItemView

app_name = "app1"

router = DefaultRouter()
router.register("items", ItemsViewset)
# router.register("add", AddView)


urlpatterns = [
    url("", include(router.urls)),
    url("todo/", CreateItemView.as_view())
]
