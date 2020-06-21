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


# class GoodsCategorySerializer(serializers.ModelSerializer):
#     merchant = MerchantSerializer(read_only=True, required=False)
#     # category 与 goods 是一对多的关系，goods为多 所以要设置 many=True
#     # goods_list 不是随便写的，是因为Goods模型中的related_name='goods_list'
#     goods_list = GoodsSerializer(many=True, required=False)
#
#     # 这个字段名最好写成这样，就可以避免自己重写create方法了
#     merchant_id = serializers.IntegerField(required=True, write_only=True)
#
#     class Meta:
#         model = GoodsCategory
#         fields = "__all__"
#
#     def validate_merchant_id(self, value):
#         if not Merchant.objects.filter(pk=value).exists():
#             raise serializers.ValidationError("商家不存在！")
#         return value
#
#     def create(self, validated_data):
#         merchant_id = validated_data.get('merchant_id')
#         merchant = Merchant.objects.get(pk=merchant_id)
#         category = GoodsCategory.objects.create(name=validated_data.get('name'), merchant=merchant)
#         return category