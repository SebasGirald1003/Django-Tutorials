from django.urls import path
from .views import homePageView, AboutPageView, ProductIndexView, ProductShowView, ProductCreateView

urlpatterns = [
    path("", homePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
]