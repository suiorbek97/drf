from rest_framework import serializers
from news.models import News


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
