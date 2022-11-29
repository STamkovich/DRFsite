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
        w = Women.objects.all()  # формируем queryset
        return Response({'posts': WomenSerializer(w, many=True).data})  # many=True говорит о том что бы сериализатор
        # брал все записи, а не одну
        # data это словарь из преобразованных данных из таблицы Women

    def post(self, request):  # request содержит все параметры POST запроса
        serializer = WomenSerializer(data=request.data)  # создали сериализатор на основе тех данных что поступили с
        # пост запросом
        serializer.is_valid(raise_exception=True)  # проверка корректности принятых данных

        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id'],
        )
        return Response({'posts': WomenSerializer(post_new).data})
        # return Response({'posts': model_to_dict(post_new)})  # model_to_dict преобразовывает объект класса в словарь

    # метод для изменения данных
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)  # идентификатор записи которую нужно поменять
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exists'})

        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    # метод для удаления данных
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)  # идентификатор записи которую нужно поменять
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        # код для удаления записи

        return Response({'post': 'delete post' + str(pk)})
