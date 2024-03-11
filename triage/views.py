from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Triage, RioDeJaneiro, Ceara, SaoPaulo
from .serializers import TriageSerializer, RioDeJaneiroSerializer, CearaSerializer, SaoPauloSerializer

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

    def get_queryset(self):
        user_triage_type = self.request.user.triage_type

        return USER_TRIAGE_TYPE[user_triage_type]['model'].object.filter(user=self.request.user)
