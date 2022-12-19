from django.urls import path
from work_card import views

urlpatterns = [
    path('card/<int:pk>/activate/', views.activate_card, name='activate_card'),
    path('card/<int:pk>/deactivate/', views.deactivate_card, name='deactivate_card'),
    path('card/<int:pk>/delete/', views.delete_creditcard, name='delete_creditcard'),
    path('card/<int:pk>/profile/', views.show_profile_card, name='show_profile_card'),
    path('card/generate/', views.generate, name='generate'),
    path('card/checkdata/', views.check_date_activity_card, name='check_date_activity_card'),
    path('', views.get_creditcards, name='get_creditcards'),
]