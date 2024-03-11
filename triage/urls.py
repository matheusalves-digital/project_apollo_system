from django.urls import path
from .views import TriageCreateView, TriageListCreateView, TriageDetailView

urlpatterns = [
    path('create_triage/', TriageCreateView.as_view(), name='triage-create'),
    path('create/', TriageListCreateView.as_view(), name='triage-list-create'),
    path('<str:pk>/', TriageDetailView.as_view(), name='triage-detail'),
]
