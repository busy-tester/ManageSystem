from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from systemuser.common import response
from systemuser import models
import jwt
from rest_framework.authentication import get_authorization_header
from django.conf import settings
from systemuser.common import serializers
from systemuser.common.authentication import generate_jwt, JWTAuthentication


# Create your views here.


class LoginView(APIView):
    """
    登录视图
    {
        "username": "zouzou",
        "passwoed": "123456"

    }
    """

    def post(self, request):
        try:
            username = request.data["username"]
            password = request.data["password"]
        except KeyError:
            return Response(response.KEY_MISS)
        user = models.Account.objects.filter(username=username, password=password).first()

        if not user:
            return Response(response.LOGIN_FAILED)
        token = generate_jwt(models.Account.objects.filter(username=username).first())
        response.LOGIN_SUCCESS["data"] = {"token": token}
        return Response(response.LOGIN_SUCCESS)


class Userinfo(APIView):
    """获取用户信息 Authorization"""

    authentication_classes = [JWTAuthentication, ]

    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', '')  # 获取token，django会转为大写
        auth = token.split()  # token为一个列表
        jwt_token = auth[1]  # 1 是Authorization里JWT 后面的
        jwt_info = jwt.decode(jwt_token, settings.SECRET_KEY)
        user_id = jwt_info.get("userId")  # 得到用户id
        nick_name = models.Account.objects.filter(id=user_id).first()
        nick_name = nick_name.nick_name
        response.USERINFO_SUCCESS["data"] = {"id": user_id, "nickname": nick_name}
        return Response(response.USERINFO_SUCCESS)
