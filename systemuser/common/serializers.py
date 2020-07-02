from rest_framework import serializers
from systemuser import models


class UserInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = "__all__"
