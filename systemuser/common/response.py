KEY_MISS = {
    "code": "3100",
    "success": False,
    "msg": "请求数据非法"
}

SYSTEM_ERROR = {
    "code": "9999",
    "success": False,
    "msg": "System Error"
}

LOGIN_FAILED = {
    "code": "3103",
    "success": False,
    "msg": "用户名或密码错误"
}

TOKEN_ERROR = {
    "code": "3104",
    "success": False,
    "msg": "token错误"
}

LOGIN_SUCCESS = {
    "code": "2001",
    "success": True,
    "msg": "login success"
}

USERINFO_SUCCESS = {
    "code": "2001",
    "success": True,
    "msg": "",
}

LOGOUT_SUCCESS = {
    "code": "2001",
    "success": True,
    "msg": "退出登录成功",
}

LOGOUT_FAILED = {
    "code": "3001",
    "success": False,
    "msg": "退出登录失败",
}

LOGOUT_ERROR = {
    "code": "500",
    "success": False,
    "msg": "系统错误",
}

REGISTER_EXIST = {
    "code": "4001",
    "success": False,
    "msg": "邮箱已被注册",
}

REGISTER_SUCCESS = {
    "code": "2001",
    "success": True,
    "msg": "注册成功",
}

REGISTER_USERNAME_EXIST = {
    "code": "3101",
    "success": False,
    "msg": "用户名已被注册"
}

REGISTER_FAILD = {
    "code": "4002",
    "success": False,
    "msg": "注册失败，请稍后重试",
}

CHECK_PWD_FAILD = {
    "code": "3101",
    "success": False,
    "msg": "密码错误"
}

CHECK_PWD_SUCCESS = {
    "code": "2000",
    "success": True,
    "msg": "密码正确"
}

UPDATE_PWD_FAILD = {
    "code": "3101",
    "success": False,
    "msg": "修改密码失败"
}

UPDATE_PWD_SUCCESS = {
    "code": "2000",
    "success": True,
    "msg": "修改密码成功，请重新登录"
}
