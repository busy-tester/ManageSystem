from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from systemapp.models import Supplier
from systemapp.untils import serializers
from systemapp.untils import response
from systemapp.untils import pagination
from systemuser.common.authentication import JWTAuthentication


class SupplierView(APIView):
    """
    供应商管理
    {

        "supplier_name": "张三",
        "contacts": "李四",
        "contacts_iphone": "171212323233",
        "remarks": "我是备注"

    }
    """
    authentication_classes = [JWTAuthentication, ]

    def post(self, request):
        supplier_name = request.data.get('supplier_name')
        name_obj = Supplier.objects.filter(supplier_name=supplier_name).exists()
        if name_obj:
            return Response(response.SUPPLIER_EXIST)
        ser_obj = serializers.SupplierSerializer(data=request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(response.SUPPLIER_SUCCESS)
        else:
            return Response(response.SUPPLIER_FAILD)

    def get(self, request):
        # http://127.0.0.1:8081/api/manage/supplier
        supplier_id = request.query_params.get('id')
        supplier_obj = Supplier.objects.filter(id=supplier_id).first()
        if not supplier_obj:
            return Response(response.SUPPLIER_NOT_EXIST)
        ser_obj = serializers.SupplierSerializer(supplier_obj)
        res = {
            "code": "2001",
            "success": True,
            "msg": "",
            "data": ser_obj.data
        }
        # 返回的是 res 了，不在是ser_obj.data
        return Response(res)

    def put(self, request):
        supplier_id = request.data.get('id')
        supplier_obj = Supplier.objects.filter(id=supplier_id).first()
        if not supplier_obj:
            return Response(response.SUPPLIER_NOT_EXIST)
        request.data.pop("update_time")
        request.data.pop("create_time")
        ser_obj = serializers.SupplierSerializer(instance=supplier_obj, data=request.data, partial=True)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(response.UPDATE_SUCCESS)
        return Response(response.UPDATE_FAILD)

    def delete(self, request):
        supplier_id = request.query_params.get('id')
        supplier_obj = Supplier.objects.filter(id=supplier_id).first()
        if not supplier_obj:
            return Response(response.SUPPLIER_NOT_EXIST)
        try:
            supplier_obj.delete()
            return Response(response.DELETE_SUCCESS)
        except Exception:
            return Response(response.DELETE_FAILD)


class SearchSupplierView(APIView):
    """http://127.0.0.1:8081/api/manage/search/supplier?page=1&size=30"""
    authentication_classes = [JWTAuthentication, ]

    def post(self, request):
        supplier_name = request.data.get('supplier_name')
        contacts = request.data.get('contacts')
        contacts_iphone = request.data.get('contacts_iphone')
        queryset = Supplier.objects.all()
        if supplier_name:
            queryset = queryset.filter(supplier_name__contains=supplier_name).order_by('-update_time')  # 更新时间倒序排序
        if contacts:
            queryset = queryset.filter(contacts__contains=contacts).order_by('-update_time')  # 更新时间倒序排序
        if contacts_iphone:
            queryset = queryset.filter(contacts_iphone__contains=contacts_iphone).order_by('-update_time')  # 更新时间倒序排序

        if not supplier_name and not contacts and not contacts_iphone:
            queryset = Supplier.objects.all().order_by('-update_time')  # 更新时间倒序排序
        total_num = queryset.filter().count()
        page_obj = pagination.MyPaginator()  # 分页
        page_data = page_obj.paginate_queryset(queryset, request)
        ser_obj = serializers.SupplierSerializer(page_data, many=True)  # 将分页的数据序列化

        res = {
            "code": "2001",
            "success": True,
            "msg": "",
            "total": total_num,
            "data": ser_obj.data
        }
        # 返回的是 res 了，不在是ser_obj.data
        return Response(res)
