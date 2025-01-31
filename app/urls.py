from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    HomePageView,
    PetProfileListView, PetProfileDetailView, PetProfileCreateView, PetProfileUpdateView, PetProfileDeleteView,
    ServicesListView, ServicesDetailView, ServicesCreateView, ServicesUpdateView, ServicesDeleteView,
    AppointmentListView, AppointmentDetailView, AppointmentCreateView, AppointmentUpdateView, AppointmentDeleteView,
    PetRecordListView, PetRecordDetailView, PetRecordCreateView, PetRecordUpdateView, PetRecordDeleteView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),

    path('pet-profile/', PetProfileListView.as_view(), name='pet_profile_list'),
    path('pet-profile/<int:pk>/', PetProfileDetailView.as_view(), name='pet_profile_detail'),
    path('pet-profile/create/', PetProfileCreateView.as_view(), name='pet_profile_create'),
    path('pet-profile/<int:pk>/update/', PetProfileUpdateView.as_view(), name='pet_profile_update'),
    path('pet-profile/<int:pk>/delete/', PetProfileDeleteView.as_view(), name='pet_profile_delete'),
    
    path('services/', ServicesListView.as_view(), name='services_list'),
    path('services/<int:pk>/', ServicesDetailView.as_view(), name='services_detail'),
    path('services/create/', ServicesCreateView.as_view(), name='services_create'),
    path('services/<int:pk>/update/', ServicesUpdateView.as_view(), name='services_update'),
    path('services/<int:pk>/delete/', ServicesDeleteView.as_view(), name='services_delete'),

    path('appointments/', AppointmentListView.as_view(), name='appointment_list'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('appointments/create/', AppointmentCreateView.as_view(), name='appointment_create'),
    path('appointments/<int:pk>/update/', AppointmentUpdateView.as_view(), name='appointment_update'),
    path('appointments/<int:pk>/delete/', AppointmentDeleteView.as_view(), name='appointment_delete'),

    path('pet-record/', PetRecordListView.as_view(), name='pet_record_list'),
    path('pet-record/<int:pk>/', PetRecordDetailView.as_view(), name='pet_record_detail'),
    path('pet-record/create/', PetRecordCreateView.as_view(), name='pet_record_create'),
    path('pet-record/<int:pk>/update/', PetRecordUpdateView.as_view(), name='pet_record_update'),
    path('pet-record/<int:pk>/delete/', PetRecordDeleteView.as_view(), name='pet_record_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
