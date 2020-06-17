from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from systemapp.models import Staff
from systemapp.untils import serializers
from systemapp.untils import response
from systemapp.untils import pagination
from systemuser.common.authentication import JWTAuthentication


class StaffView(APIView):
    """
    员工管理
        {

        "account":"1232",
        "name":"李四",
        "age": "12",
        "iphone": "17111111111",
        "salary":"1212",
        "entry_time":"1993-2-21"

    }
    """
    authentication_classes = [JWTAuthentication, ]

    def post(self, request):
        name = request.data.get('name')
        name_obj = Staff.objects.filter(name=name).exists()
        if name_obj:
            return Response(response.STAFF_EXIST)
        ser_obj = serializers.StaffSerializer(data=request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(response.STAFF_SUCCESS)
        else:
            return Response(response.STAFF_FAILD)

    def get(self, request):
        # http://127.0.0.1:8081/api/manage/supplier
        staff_id = request.query_params.get('id')
        staff_obj = Staff.objects.filter(id=staff_id).first()
        if not staff_obj:
            return Response(response.SUPPLIER_NOT_EXIST)
        ser_obj = serializers.StaffSerializer(staff_obj)
        res = {
            "code": "2001",
            "success": True,
            "msg": "",
            "data": ser_obj.data
        }
        # 返回的是 res 了，不在是ser_obj.data
        return Response(res)

    def put(self, request):
        staff_id = request.data.get('id')
        staff_obj = Staff.objects.filter(id=staff_id).first()
        if not staff_obj:
            return Response(response.STAFF_NOT_EXIST)
        # request.data.pop("update_time")
        # request.data.pop("create_time")
        ser_obj = serializers.StaffSerializer(instance=staff_obj, data=request.data, partial=True)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(response.UPDATE_SUCCESS)
        return Response(response.UPDATE_FAILD)

    def delete(self, request):
        staff_id = request.query_params.get('id')
        staff_obj = Staff.objects.filter(id=staff_id).first()
        if not staff_obj:
            return Response(response.STAFF_NOT_EXIST)
        try:
            staff_obj.delete()
            return Response(response.DELETE_SUCCESS)
        except Exception:
            return Response(response.DELETE_FAILD)


class SearchStaffView(APIView):
    """http://127.0.0.1:8081/api/manage/search/staff?page=1&size=30"""
    authentication_classes = [JWTAuthentication, ]

    def post(self, request):
        account = request.data.get('account')
        name = request.data.get('name')
        queryset = Staff.objects.all()
        if account:
            queryset = queryset.filter(account__contains=account).order_by('-update_time')  # 更新时间倒序排序
        if name:
            queryset = queryset.filter(name__contains=name).order_by('-update_time')  # 更新时间倒序排序

        if not account and not name:
            queryset = Staff.objects.all().order_by('-update_time')  # 更新时间倒序排序
        total_num = queryset.filter().count()
        page_obj = pagination.MyPaginator()  # 分页
        page_data = page_obj.paginate_queryset(queryset, request)
        ser_obj = serializers.StaffSerializer(page_data, many=True)  # 将分页的数据序列化

        res = {
            "code": "2001",
            "success": True,
            "msg": "",
            "total": total_num,
            "data": ser_obj.data
        }
        # 返回的是 res 了，不在是ser_obj.data
        return Response(res)
