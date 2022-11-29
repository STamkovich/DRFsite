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

        # переопределённый метод для добавления записи
        @staticmethod
        def create(validate_data):
            return Women.objects.create(**validate_data)
        # в таком случае в представлении post_new не нужен, а нужно просто вызвать метод save() и вернуть
        # serializer.data

        # переопределение метода update для изменения существующих данных
        def update(self, instance, validated_data): # instance - ссылка на объект модели validated_data - словарь из проверянных данных
            instance.title = validated_data.get("title", instance.title)
            instance.content = validated_data.get("content", instance.content)
            instance.time_update = validated_data.get("time_update", instance.time_update)
            instance.is_published = validated_data.get("is_published", instance.is_published)
            instance.cat_id = validated_data.get("cat_id", instance.cat_id)
            instance.save()
            return instance



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
#     model_sr = WomenSerializer(model) создание объекта сериализатора
#     print(model_sr.data, type(model_sr.data)) объект сериализации
#     json = JSONRenderer().render(model_sr.data) перевод в байтовую  JSON строку
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
