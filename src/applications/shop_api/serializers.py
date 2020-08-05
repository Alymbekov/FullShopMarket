from rest_framework import serializers
from applications.users.models import Profile, User
from applications.products.models import Product


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    profiles = ProfileSerializer()
    class Meta:
        model = User
        fields = (
            'id', 'username', 'profiles'
            )


class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields = '__all__'

