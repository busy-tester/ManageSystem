from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from systemapp.models import Member, Supplier, Goods, Staff
from systemapp.untils import serializers
from systemapp.untils import response
from systemapp.untils import pagination
from systemuser.common.authentication import JWTAuthentication


class TotalView(APIView):
    """获取对应的总数"""

    def get(self, request):
        count_num = []
        count_num.append(Member.objects.all().count())
        count_num.append(Supplier.objects.all().count())
        count_num.append(Goods.objects.all().count())
        count_num.append(Staff.objects.all().count())
        res = {

            "data": count_num
        }
        return Response(res)
