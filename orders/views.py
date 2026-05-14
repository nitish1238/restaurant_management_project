from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Coupon
class CouponVaildationView(APIView):
    def post(self,request):
        code=request.data.get("code")
        if not code:
            return Response({"error":"Coupon code is required."},
            status=status.HTTP_400_BAD_REQUEST)
        today=date.today()
        try:
            coupon =Coupon.objects.get(
                code=code,is_active=True,
                valid_from_lte=today,
                valid_until_gte=today)
        expect Coupon.DoesNotExist:
            return Response({"error":"Invalid or expired coupon."},
            status=status.HTTP_400_BAD_REQUEST
            )
        return Response({
            "valid":True,
            "code":coupon.code
            "discount_percentage":coupon.discount_percentage
        },status=status.HTTP_200_OK)
