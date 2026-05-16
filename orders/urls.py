from django.urls import path
from .views import CouponValidationView,OrderHistoryView

urlpatterns = [
    path("coupons/validate",CouponValidationView.as_view(),name="coupon-validate"),
    path("history/",OrderHistoryView.as_view(),name="order-history"),
    
]