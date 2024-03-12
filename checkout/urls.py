from django.urls import path 
from checkout.views import course_access, create_payment
from checkout.webhook import strip_webhook

urlpatterns = [
    path('create-payment-intent/<int:pk>/', create_payment, name='create-payment-intent'),
    path('stripe/webhook/', strip_webhook),
    path('<int:cid>/', course_access, name='course/access'),
]


