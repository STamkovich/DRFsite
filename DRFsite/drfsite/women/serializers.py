import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women


# сериализатор на основе моделей
class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = '__all__'
        # fields = ('title', 'content') пля которые будут обратно отправляться пользователю
        time_create = serializers.DateTimeField(read_only=True) # указать сериализаторы что добавление этих записей только для чтения
        time_update = serializers.DateTimeField(read_only=True)

# базовый принцип сериализатора(то-есть как он работает под капотом)
# class WomenModel:
#     def __int__(self, title, content):
#         self.title = title
#         self.content = content
#
#
# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField
#
#
# def encode():
#     model = WomenModel('Angelina Joli', 'Content: Angelina Joli')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data))
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# # обратное преобразование из JSON строки в объект класса WomenModel
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Angelina Joli", "content":"Content: Angelina Joli"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
