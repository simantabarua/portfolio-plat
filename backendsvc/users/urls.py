from django.urls import path
from .views import LogInAPIView, RegisterAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='regster-api-view'),
    path('login/', LogInAPIView.as_view(), name='login-api')
]