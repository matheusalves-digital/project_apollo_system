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
    }
}

class TriageCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        user_triage_type = self.request.user.triage_type
        serializer_class = USER_TRIAGE_TYPE.get(user_triage_type, {}).get('serializer', TriageSerializer)

        return serializer_class

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

class TriageListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        user_triage_type = self.request.user.triage_type
        return USER_TRIAGE_TYPE[user_triage_type]['serializer']

    def get_queryset(self):
        user_triage_type = self.request.user.triage_type
        model = USER_TRIAGE_TYPE[user_triage_type]['model']
        return model.objects.filter(user=self.request.user)

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
