from django.urls import include, path
from .views import (ProductDetailAPIView, ProductListAPIView, ManufacturerDetailAPIView,
                    ManufacturerListAPIView, UserProfileListAPIView, UserProfileDetailAPIView,
                    UserDetailAPIView, UserListAPIView, OrderListAPIView, OrderDetailAPIView,
                    CartListAPIView, CartDetailAPIView, ShippingListAPIView, ShippingDetailAPIView,
                    EffectTypeListAPIView, EffectTypeDetailAPIView, ProductImageListAPIView,
                    ProductImageDetailAPIView, ReviewListAPIView, ReviewDetailAPIView,
                    ReviewLikeAPIView, ProductFavouriteAPIView, ProductAddToCartAPIView,
                    ProductRemoveFromCartAPIView, ProductSubtractFromCartAPIView,
                    CartItemDetailAPIView, CartItemListAPIView, DiscountDetailAPIView,
                    DiscountListAPIView, AddressDetailAPIView, AddressListAPIView,
                    CartClearAPIView, OrderItemDetailAPIView, OrderItemListAPIView,
                    get_csrf_token)

app_name="api"
urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name="api_product_list"),
    path('products/<slug:slug>/', ProductDetailAPIView.as_view(), name="api_product_detail"),
    path('products/<slug:slug>/favourite', ProductFavouriteAPIView.as_view(), name="api_product_favourite"),
    path('products/<slug:slug>/add_cart', ProductAddToCartAPIView.as_view(), name="api_product_tocart"),
    path('products/<slug:slug>/subtract_cart', ProductSubtractFromCartAPIView.as_view(), name="api_product_fromcart"),
    path('products/<slug:slug>/remove_cart', ProductRemoveFromCartAPIView.as_view(), name="api_product_fromcart"),
    
    path('manufacturers/', ManufacturerListAPIView.as_view(), name="api_man_list"),
    path('manufacturers/<slug:slug>/', ManufacturerDetailAPIView.as_view(), name="api_man_detail"),
    path('users/', UserListAPIView.as_view(), name="api_user_list"),
    path('users/<str:username>/', UserDetailAPIView.as_view(), name="api_user_detail"),
    path('profiles/', UserProfileListAPIView.as_view(), name="api_profile_list"),
    path('profiles/<slug:slug>/', UserProfileDetailAPIView.as_view(), name="api_profile_detail"),

    path('orders/', OrderListAPIView.as_view(), name="api_order_list"),
    path('orders/<int:pk>/', OrderDetailAPIView.as_view(), name="api_order_detail"),
    path('orders/<int:pk>/items/', OrderItemListAPIView.as_view(), name="api_order_item_list"),
    path('order_items/<int:pk>/', OrderItemDetailAPIView.as_view(), name="api_order_item_detail"),    
   
    path('carts/', CartListAPIView.as_view(), name="api_cart_list"),
    path('carts/<slug:slug>/', CartDetailAPIView.as_view(), name="api_cart_detail"),
    path('carts/<slug:slug>/items/', CartItemListAPIView.as_view(), name="api_cart_item_list"),
    path('carts/<slug:slug>/clear/', CartClearAPIView.as_view(), name="api_cart_clear"),
    path('shippings/', ShippingListAPIView.as_view(), name="api_shipping_list"),
    path('shippings/<slug:slug>/', ShippingDetailAPIView.as_view(), name="api_shipping_detail"),
    path('effecttypes/', EffectTypeListAPIView.as_view(), name="api_effecttype_list"),
    path('effecttypes/<slug:slug>/', EffectTypeDetailAPIView.as_view(), name="api_effecttype_detail"),
    path('productimages/', ProductImageListAPIView.as_view(), name="api_productimage_list"),
    path('productimages/<slug:slug>/', ProductImageDetailAPIView.as_view(), name="api_productimage_detail"),
    path('reviews/', ReviewListAPIView.as_view(), name="api_review_list"),
    path('reviews/<slug:slug>/', ReviewDetailAPIView.as_view(), name="api_review_detail"),
    path('reviews/<slug:slug>/like', ReviewLikeAPIView.as_view(), name="api_review_like"),
    
    path('get_token', get_csrf_token, name="get_token"),

    path('discounts/', DiscountListAPIView.as_view(), name="api_discount_list"),
    path('discounts/<slug:slug>/', DiscountDetailAPIView.as_view(), name="api_discount_detail"),

    path('address/', AddressListAPIView.as_view(), name="api_discount_list"),
    path('address/<slug:slug>/', AddressDetailAPIView.as_view(), name="api_discount_detail"),
]