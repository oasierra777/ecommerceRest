from django.urls import path

from apps.cart.views import AddItemView
from apps.cart.views import EmptyCartView
from apps.cart.views import GetItemTotalView
from apps.cart.views import GetItemsView
from apps.cart.views import GetTotalView
from apps.cart.views import RemoveItemView
from apps.cart.views import SynchCartView
from apps.cart.views import UpdateItemView

urlpatterns = [
    path('cart-items', GetItemsView.as_view()),
    path('add-item', AddItemView.as_view()),
    path('get-total', GetTotalView.as_view()),
    path('get-item-total', GetItemTotalView.as_view()),
    path('update-item', UpdateItemView.as_view()),
    path('remove-item', RemoveItemView.as_view()),
    path('empty-cart', EmptyCartView.as_view()),
    path('synch', SynchCartView.as_view()),
]