from django.template.response import TemplateResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import Pars
from .serializers import ParsSerializer


def index(request):
    return TemplateResponse (request, "api/index.html")


class ParsView(ListCreateAPIView):
    queryset = Pars.objects.all()
    serializer_class = ParsSerializer


class SingleParsView(RetrieveUpdateAPIView):
    queryset = Pars.objects.all()
    serializer_class = ParsSerializer


class SingleParsView(RetrieveUpdateDestroyAPIView):
    queryset = Pars.objects.all()
    serializer_class = ParsSerializer

