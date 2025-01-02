from django.urls import path
from .views import HomePageView, LoginPageView, RegisterPageView, AdminHomePageView, CustomerHomePageView, CustomerPetsPageView, CustomerPetDetailView, CustomerPetCreateView, CustomerPetUpdateView, CustomerPetDeleteView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('admin-dashboard/', AdminHomePageView.as_view(), name='admin-dashboard'),
    path('customer-dashboard/', CustomerHomePageView.as_view(), name='customer-dashboard'),
    path('customer-pets/', CustomerPetsPageView.as_view(), name='customer-pets'),
    path('customer-petdetail/<int:pk>/', CustomerPetDetailView.as_view(), name='pet-detail'),
    path('customer-addpet/', CustomerPetCreateView.as_view(), name='add-pet'),
    path('pets/<int:pk>/update/', CustomerPetUpdateView.as_view(), name='update-pet'),
    path('pets/<int:pk>/delete/', CustomerPetDeleteView.as_view(), name='delete-pet')
]