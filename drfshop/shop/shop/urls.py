from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from product.views import *
from rest_framework import routers

app_name = 'product'


urlpatterns = [
#_____________________________________________________________

                         # DRF Auth
# ______________________________________________________________

     path('admin/', admin.site.urls),
     path('api/v1/drf-auth/', include('rest_framework.urls')),

#______________________________________________________________

                         #Главнач страница с продуктами
#______________________________________________________________

     path('api/v1/shop/productlist', ProductAPIList.as_view()),
     path('api/v1/shop/productlist/<int:pk>/', ProductAPIUpdate.as_view()),
     path('api/v1/shop/productlist/delete/<int:pk>/', ProductAPIDestroy.as_view()),


#______________________________________________________________

                         # Корзина
#______________________________________________________________
     path('api/v1/shop/carts', ListCart.as_view(), name='allcarts'),
     path('api/v1/shop/carts/<int:pk>', DetailCart.as_view(), name='cart_detail'),
     path('api/v1/shop/productlist/search/custom/', ProductListDetailFilter.as_view(), name='product_search'),

#______________________________________________________________

                       #Djoser токен
#______________________________________________________________
     path('api/v1/auth/', include('djoser.urls')),
     re_path(r'^auth/', include('djoser.urls.authtoken')),

#______________________________________________________________

                        #JWT токен
#______________________________________________________________
     path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('api/v1/token/verify', TokenVerifyView.as_view(), name='token_verify'),

#______________________________________________________________

                         #Подключение картинок
#______________________________________________________________

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#     # Postman: POST http://127.0.0.1:8000/auth/token/login/





