from rest_framework import serializers
from systemapp.models import Member


class MemberSerializer(serializers.ModelSerializer):
    """会员序列化"""
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Member
        fields = "__all__"
