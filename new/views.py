from .models import New
from .serializers import NewsSerializer
from rest_framework.generics import ListAPIView, CreateAPIView,  RetrieveDestroyAPIView, RetrieveUpdateAPIView
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.


class NewsListViews(ListAPIView):
    serializer_class = NewsSerializer
    queryset = New.objects.all()

class NewCreateViews(CreateAPIView):
    # permission_classes = IsAuthenticated
    serializer_class = NewsSerializer
    queryset = New.objects.all()

class NewDestroyViews(RetrieveDestroyAPIView):
    # permission_classes = IsAdminUser
    serializer_class = NewsSerializer
    queryset = New.objects.all()


class NewUpdateViews(RetrieveUpdateAPIView):
    # permission_classes = IsAdminUser
    serializer_class = NewsSerializer
    queryset = New.objects.all()



