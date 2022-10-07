from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response

from .models import Women
from .serializers import WomenSerializer
from rest_framework.views import APIView


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# Принцип работы представлений

class WomenAPIView(APIView):
    @staticmethod
    def get(request):  # request содержит все параметры GET запроса
        w = Women.objects.all()
        return Response({'posts': WomenSerializer(w, many=True).data})  # many=True говорит о том что бы сериализатор
        # брал все записи, а не одну
        # data это словарь из преобразованных данных из таблицы Women

    def post(self, request):  # request содержит все параметры POST запроса
        serializer = WomenSerializer(data=request.data) # создали сериализатор на основе тех данных что поступили с
        # пост запросом
        serializer.is_valid(raise_exception=True)  # проверка корректности принятых данных

        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id'],
        )
        return Response({'posts': WomenSerializer(post_new).data})
        # return Response({'posts': model_to_dict(post_new)})  # model_to_dict преобразовывает объект класса в словарь
