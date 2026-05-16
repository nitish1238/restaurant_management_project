from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Coupon
from .models import Order
from .serializers import OrderSerializer
class CouponValidationView(APIView):
    def post(self,request):
        code=request.data.get("code")
        if not code:
            return Response({"error":"Coupon code is required."},
            status=status.HTTP_400_BAD_REQUEST)
        today=date.today()
        try:
            coupon =Coupon.objects.get(
                code=code,is_active=True,
                valid_from__lte=today,
                valid_until__gte=today)
        except Coupon.DoesNotExist:
            return Response({"error":"Invalid or expired coupon."},
            status=status.HTTP_400_BAD_REQUEST
            )
        return Response({
            "valid":True,
            "code":coupon.code,
            "discount_percentage":coupon.discount_percentage
        },status=status.HTTP_200_OK)
class OrderHistoryView(ListAPIView):
    serializer_class=OrderSerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by("-id")
