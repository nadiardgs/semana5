from django.urls import include, path, re_path
from rest_framework import routers
from product_api import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductAPIViewSet)
#router.register(r'categories', views.CategoryAPI)

urlpatterns = [
    path('', include(router.urls)),
    path('categories/', views.CategoryListOnlyAPIView.as_view()),
    re_path(r'vendas/(?P<pk>\d+)?', views.OrderAPIView.as_view()),
]