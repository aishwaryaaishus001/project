from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home),
    path('programmes', views.programmes),
    path('semester', views.semester),
    path('feedback', views.feedback),
    path('cs/', views.cs_view, name='cs'),
]