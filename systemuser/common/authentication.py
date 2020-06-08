import jwt
import time
from django.conf import settings
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from systemuser.models import Account


# 加密
def generate_jwt(user):
    timestamp = int(time.time()) + 60 * 60 * 24 * 7  # 七天过期时间
    # 因为 Jwt.encode返回的是bytes数据类型，因此需要decode解码成str类型
    # 使用settings下的SECRET_KEY为密钥
    return jwt.encode({"userId": user.pk, "exp": timestamp}, settings.SECRET_KEY).decode('utf-8')


# 解密
class JWTAuthentication(BaseAuthentication):
    """
        Authorization: JWT 401f7ac837da42b97f613d789819ff93537bee6a
    """
    keyword = 'JWT'
    model = None

    def authenticate(self, request):
        auth = get_authorization_header(request).split()  # auth为一个列表

        # 判断auth为空或者列表的第一个元素不为jwt
        if not auth or auth[0].lower() != self.keyword.lower().encode():
            msg = 'token不合法'
            raise exceptions.AuthenticationFailed(msg)

        if len(auth) == 1:
            msg = 'Authorization 不可用'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Authorization 不可用, 应该提供一个空格'
            raise exceptions.AuthenticationFailed(msg)

        try:
            jwt_token = auth[1]  # 1 是Authorization里JWT 后面的
            jwt_info = jwt.decode(jwt_token, settings.SECRET_KEY)
            userId = jwt_info.get('userId')  # 得到用户id，因为加密是拿用户id加密的
            try:
                user = Account.objects.get(pk=userId)
                # print(user, userId)  # 获取用户 id
            except:
                msg = '用户不存在'
                raise exceptions.AuthenticationFailed(msg)

        except jwt.ExpiredSignature:  # 超过了 7 天
            msg = 'Token已过期'
            raise exceptions.AuthenticationFailed(msg)

        except Exception:
            msg = 'Token不合法'
            raise exceptions.AuthenticationFailed(msg)
