from rest_framework import serializers
from systemapp.models import Member


class MemberSerializer(serializers.ModelSerializer):
    """会员序列化"""
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    # member_birthday = serializers.DateField(read_only=True)
    # phone_number = serializers.IntegerField(read_only=True)
    # card_money = serializers.IntegerField(read_only=True)
    # Available_integral = serializers.IntegerField(read_only=True)
    # member_address = serializers.CharField(read_only=True)


    class Meta:
        model = Member
        fields = "__all__"

