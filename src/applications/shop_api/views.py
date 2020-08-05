from django.shortcuts import render
from rest_framework  import generics, viewsets, mixins 
from applications.users.models import Profile
from rest_framework.response import Response
from .serializers import UserSerializer, ProductSerializer
from django.contrib.auth.models  import User
from applications.shop_api.permissions import IsAuthorPermission
from rest_framework.permissions import IsAuthenticated
from applications.products.models import Product


class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthorPermission, IsAuthenticated, )

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.request.user.pk)
        if queryset.count() > 1:
            raise ValueError("Error")
        return queryset


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = None
    permission_classes = (IsAuthorPermission, )



