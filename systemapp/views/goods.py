from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from systemapp.models import Goods
from systemapp.untils import serializers
from systemapp.untils import response
from systemapp.untils import pagination
from systemuser.common.authentication import JWTAuthentication


class GoodsView(APIView):
    """
    员工管理
    {

        "name":"黄瓜",
        "code": "12",
        "specs": "234",
        "retail_price":"1212",
        "buying_price":"1991",
        "amount":"23",
        "supplier":"1"

    }
    """
    authentication_classes = [JWTAuthentication, ]

    def post(self, request):
        name = request.data.get('name')
        name_obj = Goods.objects.filter(name=name).exists()
        if name_obj:
            return Response(response.GOODS_EXIST)
        ser_obj = serializers.GoodsSerializer(data=request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(response.GOODS_SUCCESS)
        else:
            return Response(response.GOODS_FAILD)
