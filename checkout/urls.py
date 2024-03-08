from django.urls import path 
from checkout.views import course_access, create_payment

urlpatterns = [
    path('create-payment-intent/<int:pk>/', create_payment, name='create-payment-intent'),
    path('<int:cid>/', course_access, name='course/access'),
]


