from django.urls import path
from .views import (
    ProfileListCreateView,
    ProfileRetrieveUpdateDestroyView,
    TimeEntryListCreateView,
    TimeEntryRetrieveUpdateDestroyView
)

urlpatterns = [
    path('profiles/', ProfileListCreateView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', ProfileRetrieveUpdateDestroyView.as_view(), name='profile-detail'),
    path('time-entries/', TimeEntryListCreateView.as_view(), name='timeentry-list-create'),
    path('time-entries/<int:pk>/', TimeEntryRetrieveUpdateDestroyView.as_view(), name='timeentry-detail'),
]