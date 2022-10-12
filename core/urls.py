from django.contrib import admin
from django.urls import path
from qrcodes.views import GenerateCodeView, QRCodeDetailView, QRCodeListView

from users.views import LoginView, LogoutView, ProfileView, RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/register/', RegisterView.as_view()),
    path('api/v1/login/', LoginView.as_view()),
    path('api/v1/logout/', LogoutView.as_view()),

    path('api/v1/profile/', ProfileView.as_view()),

    path('api/v1/qrcodes/', QRCodeListView.as_view()),
    path('api/v1/qrcodes/<int:pk>/', QRCodeDetailView.as_view()),
    path('api/v1/qrcodes/generate/', GenerateCodeView.as_view()),
]
