from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from systemapp.models import Member
from systemapp.untils import serializers
from systemapp.untils import response
from systemapp.untils import pagination
from systemuser.common.authentication import JWTAuthentication


# Create your views here.


class MemberView(APIView):
    authentication_classes = [JWTAuthentication, ]
    """
    会员视图

    {
        "member_card":"12323123",
        "member_name":"邹邹",
        "member_birthday":"1992-02-12",
        "phone_number":"17693638363",
        "card_money":"234234",
        "Available_integral":"342342",
        "pay_type":"1",
        "member_address":"甘肃省"
    }
        """

    def post(self, request):

        MemberName = request.data.get('member_name', '')
        name_obj = Member.objects.filter(member_name=MemberName).first()
        if name_obj:
            return Response(response.MEMBER_EXIST)
        ser_obj = serializers.MemberSerializer(data=request.data)  # 获取所有数据
        if ser_obj.is_valid():
            ser_obj.save()  # 添加数据
            return Response(response.MEMBER_SUCCESS)
        else:
            # return Response(response.MEMBER_FAILD)
            return Response(response.MEMBER_FAILD)

    def get(self, request):
        # http://127.0.0.1:8081/api/manage/member?page=2&size=1
        member_id = request.query_params.get('id')
        merber_obj = Member.objects.filter(id=member_id).first()
        if not merber_obj:
            return Response(response.MEMBER_NOT_EXIST)
        ser_obj = serializers.MemberSerializer(merber_obj)
        res = {
            "code": "2001",
            "success": True,
            "msg": "",
            "data": ser_obj.data
        }
        # 返回的是 res 了，不在是ser_obj.data
        return Response(res)

    def put(self, request):
        member_id = request.data.get('id')
        member_obj = Member.objects.filter(id=member_id).first()
        if not member_obj:
            return Response(response.MEMBER_NOT_EXIST)
        request.data.pop("update_time")
        request.data.pop("create_time")
        ser_obj = serializers.MemberSerializer(instance=member_obj, data=request.data, partial=True)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(response.MEMBER_UPDATE_SUCCESS)
        return Response(response.MEMBER_UPDATE_FAILD)

    def delete(self, request):
        member_id = request.query_params.get('id')
        member_obj = Member.objects.filter(id=member_id).first()
        if not member_obj:
            return Response(response.MEMBER_NOT_EXIST)
        try:
            member_obj.delete()
            return Response(response.MEMBER_DELETE_SUCCESS)
        except Exception:
            return Response(response.MEMBER_DELETE_FAILD)


class SearchMemberView(APIView):
    authentication_classes = [JWTAuthentication, ]

    """
        搜索分页 http://127.0.0.1:8081/api/manage/search/member?page=2&size=10

        {
            "member_birthday": "",
            "member_card": "",
            "member_name": "送7",
            "pay_type": ""
        }
    """

    def post(self, request):
        member_name = request.data.get('member_name')
        member_card = request.data.get('member_card')
        pay_type = request.data.get('pay_type')
        member_birthday = request.data.get('member_birthday')
        queryset = Member.objects.all()
        if member_name:
            queryset = queryset.filter(member_name__contains=member_name).order_by('-update_time')  # 更新时间倒序排序
        if member_card:
            queryset = queryset.filter(member_card__contains=member_card).order_by('-update_time')  # 更新时间倒序排序
        if pay_type:
            queryset = queryset.filter(pay_type__contains=pay_type).order_by('-update_time')  # 更新时间倒序排序
        if member_birthday:
            queryset = queryset.filter(member_birthday=member_birthday).order_by('-update_time')  # 更新时间倒序排序
        if not member_name and not member_card and not pay_type and not member_birthday:
            queryset = Member.objects.all().order_by('-update_time')  # 更新时间倒序排序
        total_num = queryset.filter().count()
        page_obj = pagination.MyPaginator()  # 分页
        page_data = page_obj.paginate_queryset(queryset, request)
        ser_obj = serializers.MemberSerializer(page_data, many=True)  # 将分页的数据序列化

        res = {
            "code": "2001",
            "success": True,
            "msg": "",
            "total": total_num,
            "data": ser_obj.data
        }
        # 返回的是 res 了，不在是ser_obj.data
        return Response(res)
