from django.urls import path
from quize import views

urlpatterns = [
    path('account/login/', views.LoginView.as_view(), name='login'),
    path('account/logout/', views.LogoutView.as_view(), name='logout'),
    path('account/register/', views.register, name='register'),
    path('start_test/<int:pk>/', views.create_session, name='start_test'),
    path('quiz/question/<int:pk>', views.quiz, name='quiz'),
    path('complete_test/<int:pk>', views.complete_test, name='complete_test'),
    path('', views.get_testsuit, name='get_testsuit')
]