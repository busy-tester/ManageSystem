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
            return Response(response.MEMBER_FAILD)

    def get(self, request):
        # http://127.0.0.1:8081/api/manage/member?page=2&siz=1
        queryset = Member.objects.all().order_by('-update_time')  # 更新时间倒序排序
        page_obj = pagination.MyPaginator()  # 分页
        page_data = page_obj.paginate_queryset(queryset, request)
        ser_obj = serializers.MemberSerializer(page_data, many=True)  # 将分页的数据序列化

        res = {
            "code": "2001",
            "success": True,
            "msg": "",
            "data": ser_obj.data
        }
        # 返回的是 res 了，不在是ser_obj.data
        return Response(res)
