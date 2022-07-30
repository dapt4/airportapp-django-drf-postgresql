from django.urls import path
from . import views

urlpatterns = [
    path('signin', views.sigin),
    path('signup', views.signup),
    path('seat', views.seat),
    path('airplane', views.airplane),
    path('ticket', views.ticket),
    path('ticket/<int:id>', views.edit_ticket),
]
