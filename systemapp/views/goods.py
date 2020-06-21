from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from systemapp.models import Goods, Supplier
from systemapp.untils import serializers
from systemapp.untils import response
from systemapp.untils import pagination
from systemuser.common.authentication import JWTAuthentication


class GoodsView(APIView):
    """
    商品管理
    {

            "name":"巍峨",
            "code": "12",
            "specs": "234",
            "retail_price":"1212",
            "buying_price":"1991",
            "amount":"23",
            "supplier":1

    }
    """

    # authentication_classes = [JWTAuthentication, ]

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
    # 查询全部数据
    # def get(self, request):
    #     data_all = Goods.objects.all()
    #     ser_obj = serializers.GoodsSerializer(data_all, many=True)
    #     return Response(ser_obj.data)

    def get(self, request):
        # http://127.0.0.1:8081/api/manage/goods?id=1
        good_id = request.query_params.get('id')
        good_obj = Goods.objects.filter(id=good_id).first()
        if not good_obj:
            return Response(response.GOODS_NOT_EXIST)
        ser_obj = serializers.GoodsSerializer(good_obj)
        res = {
            "code": "2001",
            "success": True,
            "msg": "",
            "data": ser_obj.data
        }
        # 返回的是 res 了，不在是ser_obj.data
        return Response(res)

    def put(self, request):
        goods_id = request.data.get('id')

        goods_obj = Goods.objects.filter(id=goods_id).first()
        if not goods_obj:
            return Response(response.GOODS_NOT_EXIST)

        request.data.pop("update_time")
        request.data.pop("create_time")
        ser_obj = serializers.GoodsSerializer(instance=goods_obj, data=request.data, partial=True)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(response.UPDATE_SUCCESS)
        return Response(response.UPDATE_FAILD)

    def delete(self, request):
        goods_id = request.query_params.get('id')
        goods_obj = Goods.objects.filter(id=goods_id).first()
        if not goods_id:
            return Response(response.GOODS_NOT_EXIST)
        try:
            goods_obj.delete()
            return Response(response.DELETE_SUCCESS)
        except Exception:
            return Response(response.DELETE_FAILD)


class SearchGoodsView(APIView):
    authentication_classes = [JWTAuthentication, ]
    """
    http://127.0.0.1:8081/api/manage/search/goods?page=1&size=10
    {
        "name":"",
        "code":"",
        "supplier":2
    }
    """

    def post(self, request):
        name = request.data.get('name')
        code = request.data.get('code')
        supplier = request.data.get('supplier')
        queryset = Goods.objects.all()
        if name:
            queryset = queryset.filter(name__contains=name).order_by('-update_time')
        if code:
            queryset = queryset.filter(code__contains=code).order_by('-update_time')
        if supplier:
            queryset = queryset.filter(supplier_id=supplier).order_by('-update_time')
        if not name and not code and not supplier:
            queryset = Goods.objects.all().order_by('-update_time')  # 更新时间倒序排序
        total_num = queryset.filter().count()
        page_obj = pagination.MyPaginator()  # 分页
        page_data = page_obj.paginate_queryset(queryset, request)
        ser_obj = serializers.GoodsSerializer(page_data, many=True)  # 将分页的数据序列化

        res = {
            "code": "2001",
            "success": True,
            "msg": "",
            "total": total_num,
            "data": ser_obj.data
        }
        # 返回的是 res 了，不在是ser_obj.data
        return Response(res)
