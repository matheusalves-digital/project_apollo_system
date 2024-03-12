from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Triage, RioDeJaneiro, Ceara, SaoPaulo
from .serializers import TriageSerializer, RioDeJaneiroSerializer, CearaSerializer, SaoPauloSerializer
from django.http import Http404

USER_TRIAGE_TYPE = {
    'RioDeJaneiro': {
        'serializer': RioDeJaneiroSerializer,
        'model': RioDeJaneiro
    }, 
    'Ceara': {
        'serializer': CearaSerializer,
        'model': Ceara
    },
    'SaoPaulo': {
        'serializer': SaoPauloSerializer,
        'model': SaoPaulo
    },
    'Triage': {
        'serializer': TriageSerializer,
        'model': Triage
    }
}

class TriageCreateView(generics.CreateAPIView):
    serializer_class = TriageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TriageListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        user_triage_type = self.request.user.triage_type

        return USER_TRIAGE_TYPE[user_triage_type]['serializer']

    def get_queryset(self):
        user_triage_type = self.request.user.triage_type

        return USER_TRIAGE_TYPE[user_triage_type]['model'].objects.filter(user=self.request.user)

class TriageDetailView(generics.RetrieveAPIView):
    queryset = Triage.objects.all()
    serializer_class = TriageSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        process_number = self.kwargs.get('pk')

        try:
            triage = Triage.objects.get(number_of_process=process_number)

            return triage
        except Triage.DoesNotExist:
            raise Http404('Triage not found')

    # def get_queryset(self):
    #     user_triage_type = self.request.user.triage_type

    #     return USER_TRIAGE_TYPE[user_triage_type]['model'].object.filter(user=self.request.user)
