from django.test import TestCase

# Create your tests here.
USERINFO_SUCCESS = {
    "code": "2001",
    "success": "323",
    "msg": ""
}
USERINFO_SUCCESS['data'] = {'id': "112", 'nickname': "22"}
print(USERINFO_SUCCESS)