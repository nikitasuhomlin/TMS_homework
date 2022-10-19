from django.urls import path, include
from . import views
from store.api import api_add_subscriber

from store.controller import authview, cart, wishlist, checkout, order

urlpatterns = [
    path('', views.home, name='home'),
    path('collections', views.collections, name='collections'),
    path('collections/<str:slug>', views.collectionsview, name='collectionsview'),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productview, name='productview'),
    path('collections/submit_review/<str:cate_slug>/<str:prod_slug>', views.submit_review, name='submit_review'),

    path('product-list', views.productlistajax, name='productlistajax'),
    path('searchproduct', views.searchproduct, name='searchproduct'),

    path('register/', authview.register, name='register'),
    path('login/', authview.loginpage, name='loginpage'),
    path('logout/', authview.logoutpage, name='logout'),

    path('add-to-cart', cart.addtocart, name='addtocart'),
    path('cart/', cart.viewcart, name='cart'),
    path('update-cart', cart.updatecart, name='updatecart'),
    path('cart/delete-cart-item', cart.deletecartitem, name='deletecartitem'),

    path('wishlist/', wishlist.index, name='wishlist'),
    path('add-to-wishlist', wishlist.addtowishlist, name='addtowishlist'),
    path('delete-wishlist-item', wishlist.deletewishlistitem, name='deletewishlistitem'),

    path('checkout/', checkout.index, name='checkout'),
    path('place-order/', checkout.placeorder, name='placeorder'),

    path('my-orders', order.index, name='myorders'),
    path('view-order/<str:t_no>', order.vieworder, name='orderview'),

    path('add_subscriber/', api_add_subscriber, name='api_add_subscriber'),

]