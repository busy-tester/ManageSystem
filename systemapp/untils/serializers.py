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


class GoodsSerializer(serializers.ModelSerializer):
    """商品序列化"""
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    supplier_info = serializers.SerializerMethodField(read_only=True)

    def get_supplier_info(self, obj):
        supplier_obj = obj.supplier
        return {"id": supplier_obj.id, 'name': supplier_obj.supplier_name}

    class Meta:
        model = Goods
        fields = "__all__"
        # extra_kwargs = {"supplier": {"write_only": True}}
        # depth = 1

        # fields = ["id", 'name', "code", "specs", "retail_price", "buying_price", "amount", "supplier_id", "create_time",
        #           "update_time"]
