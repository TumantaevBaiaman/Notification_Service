from django.shortcuts import render
from rest_framework import mixins, generics
from .serializers import (
    UserSerializer, PhoneSerializer,
    HourSerializer, MailingSerializer,
    MessageSerializer
)
from .models import (
    User, Phone, Hour, Mailing, Message
)


class HourView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = HourSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = Hour.objects.all()
        query = request.GET.get('id')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)


class DetailHourView(
    mixins.DestroyModelMixin, mixins.UpdateModelMixin,
    generics.RetrieveAPIView, mixins.CreateModelMixin,
    mixins.ListModelMixin
):
    permission_classes = []
    queryset = Hour.objects.all()
    serializer_class = HourSerializer

    def put(self, *args, **kwargs):
        return self.update(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.update(*args, **kwargs)


class PhoneView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = PhoneSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = Phone.objects.all()
        query = request.GET.get('id')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)


class DetailPhoneView(
    mixins.DestroyModelMixin, mixins.UpdateModelMixin,
    generics.RetrieveAPIView, mixins.CreateModelMixin,
    mixins.ListModelMixin
):
    permission_classes = []
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

    def put(self, *args, **kwargs):
        return self.update(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.update(*args, **kwargs)


class UserView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = UserSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = User.objects.all()
        query = request.GET.get('id')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)


class DetailUserView(
    mixins.DestroyModelMixin, mixins.UpdateModelMixin,
    generics.RetrieveAPIView, mixins.CreateModelMixin,
    mixins.ListModelMixin
):
    permission_classes = []
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, *args, **kwargs):
        return self.update(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.update(*args, **kwargs)


class MailingView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = MailingSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = Mailing.objects.all()
        query = request.GET.get('id')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)


class DetailMailingView(
    mixins.DestroyModelMixin, mixins.UpdateModelMixin,
    generics.RetrieveAPIView, mixins.CreateModelMixin,
    mixins.ListModelMixin
):
    permission_classes = []
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

    def put(self, *args, **kwargs):
        return self.update(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.update(*args, **kwargs)


class MessageView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = MessageSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = Message.objects.all()
        query = request.GET.get('id')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)


class DetailMessageView(
    mixins.DestroyModelMixin, mixins.UpdateModelMixin,
    generics.RetrieveAPIView, mixins.CreateModelMixin,
    mixins.ListModelMixin
):
    permission_classes = []
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def put(self, *args, **kwargs):
        return self.update(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.update(*args, **kwargs)

