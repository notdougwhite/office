from django.urls import path

from . import views

app_name = 'intake'
"""
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:case_id>/', views.detail, name='detail'),
    path('<int:case_id>/intakes/', views.intakes, name='intakes'),
]
"""
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/create/', views.CaseCreate.as_view(), name='create'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('name/', views.name, name='name'),
    # path('<int:pk>/intakes/', views.DetailView.as_view(), name='intakes'),
]