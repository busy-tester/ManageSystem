from rest_framework import serializers
from systemapp.models import Member, Supplier, Goods, Staff


class MemberSerializer(serializers.ModelSerializer):
    """会员序列化"""
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Member
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):
    """供应商序列化"""
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Supplier
        fields = "__all__"


class StaffSerializer(serializers.ModelSerializer):
    """员工序列化"""
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Staff
        fields = "__all__"
