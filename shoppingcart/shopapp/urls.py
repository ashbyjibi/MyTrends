from django.urls import path
from .import views
app_name='shopapp'
urlpatterns=[


    path('',views.allProductsCat,name='allProductsCat'),
    path('<slug:c_slug>/',views.allProductsCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodCatDetail, name='prodCatDetail'),
 ]