from madsi.models import Answer
from madsi.serializers import AnswerSerializer
from rest_framework import generics


class AnswersListView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
