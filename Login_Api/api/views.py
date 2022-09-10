from Login_Api.api.models import MyUser
from .serializers import MyUserSerializer
from rest_framework import generics

# Create your views here.
 
class MyUserList(generics.ListCreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


class MyUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer