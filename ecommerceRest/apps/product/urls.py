from django.urls import path

from apps.product.views import ListBySearchView
from apps.product.views import ListProductsView
from apps.product.views import ListRelatedView
from apps.product.views import ListSearchView
from apps.product.views import ProductDetailView

app_name = "product"

urlpatterns = [
    path('product/<productId>', ProductDetailView.as_view()),
    path('get-products', ListProductsView.as_view()),
    path('search', ListSearchView.as_view()),
    path('related/<productId>', ListRelatedView.as_view()),
    path('by/search', ListBySearchView.as_view()),
]