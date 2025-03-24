from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:pk>/', views.productDetail, name='product-detail'),
    path('category/<str:category>/', views.productCategory, name='product_category'),
    path('product/<int:pk>/', views.productDetail, name='product-details'),
    path('product/reviews/<int:pk>/', views.productReview, name='product-reviews'),
    path('product/reviews/add/<int:pk>', views.addReview, name='add-review'),
]