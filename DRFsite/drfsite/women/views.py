from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .models import Women, Category
from .serializers import WomenSerializer
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView


# В случае когда идёт дублирование кода можно использовать ViewSets
# реализация при помощи класса ModelViewSets



class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

    #  переопределяем метод для возвращенья определенного количества записей из БД
    # так же нужно добавить basename в роуты
    # def get_queryset(self):
    #   pk = self.kwargs.get("pk")

    #   if not pk:
    #       return Women.object.all()[:3]
    #   return Women.object.filter(pk=pk)

    # декоратор для добавления новый нестандартных маршрутов
    @action(methods=['get'], detail=True)  # в случае если нам нужен список чего-либо нужно использовать detail=False
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})

# class WomenApiListPagination(PageNumberPagination): #  собственный класс погинации
#     page_size = 3 # количество записей на страницу
#     page_size_query_param = 'page_size'  # дополнительный параметр для просмотра количества записей
#     max_page_size = 1000 # максимальное значение дополнительного параметра page_size

# реализация при помощи класса ListCreateAPIView  с добавлением ограничения
# class WomenAPIList(generics.ListCreateAPIView):
#    queryset = Women.objects.all()
#    serializer_class = WomenSerializer
#    permission_classes = (IsAuthenticatedOrReadOnly, )
#    pagination_class = WomenApiListPagination # подключаем наш класс пагинации
#
#
# реализация при помощи класса RetrieveUpdateAPIView с добавлением ограничения
# class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
#    queryset = Women.objects.all()
#    serializer_class = WomenSerializer
#    permission_classes = (IsOwnerOrReadOnly, )
#    authentication_classes = (TokenAuthentication, ) # каждому представлению можно прописывать аутентификацию
#
#
# реализация при помощи класса RetrieveDestroyAPIView  с добавлением ограничения
# class WomenAPIDetailView(generics.RetrieveDestroyAPIView):
#    queryset = Women.objects.all()
#    serializer_class = WomenSerializer
#    permission_classes = (IsAdminOrReadOnly, )

# Принцип работы представлений

# class WomenAPIView(APIView):
#    @staticmethod
#    def get(request):  # request содержит все параметры GET запроса
#        w = Women.objects.all()  # формируем queryset
#        return Response({'posts': WomenSerializer(w, many=True).data})  # many=True говорит о том что бы сериализатор
#        # брал все записи, а не одну
#        # data это словарь из преобразованных данных из таблицы Women
#
#    def post(self, request):  # request содержит все параметры POST запроса
#        serializer = WomenSerializer(data=request.data)  # создали сериализатор на основе тех данных что поступили с
#        # пост запросом
#        serializer.is_valid(raise_exception=True)  # проверка корректности принятых данных
#
#        post_new = Women.objects.create(
#            title=request.data['title'],
#            content=request.data['content'],
#            cat_id=request.data['cat_id'],
#        )
#        return Response({'posts': WomenSerializer(post_new).data})
#        # return Response({'posts': model_to_dict(post_new)})  # model_to_dict преобразовывает объект класса в словарь

# метод для изменения данных

# def put(self, request, *args, **kwargs):
#     pk = kwargs.get('pk', None)  # идентификатор записи которую нужно поменять
#     if not pk:
#         return Response({"error": "Method PUT not allowed"})
#
#     try:
#         instance = Women.objects.get(pk=pk)
#     except:
#         return Response({'error': 'Object does not exists'})
#
#     serializer = WomenSerializer(data=request.data, instance=instance)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response({'post': serializer.data})

# метод для удаления данных
# def delete(self, request, *args, **kwargs):
#     pk = kwargs.get('pk', None)  # идентификатор записи которую нужно удалить
#     if not pk:
#         return Response({"error": "Method DELETE not allowed"})
#
#     else:
#         pk = Women.objects.filter(pk=pk).delete()
#         return Response({'post': 'delete post' + str(pk)})
