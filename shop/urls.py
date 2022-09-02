from .import views
from django.urls import path

urlpatterns = [
   path('', views.index, name='ShopHome'),
   path('about/', views.about, name='AboutUs'),
   path('contact/', views.contact, name='ContactUs'),
   path('track/', views.track, name='TrackingStatus'),
   path('search/', views.search, name='SearchItems'),
   path('products/<int:myid>', views.productsView, name='ProductsPage'),
   path('checkout/', views.checkOut, name='CheckoutPage'),
]