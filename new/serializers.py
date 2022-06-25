from .models import New

from rest_framework import  serializers

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = New
        fields = ('id', 'title', 'content', 'auther', 'time_add', 'image')
