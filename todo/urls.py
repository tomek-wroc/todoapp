from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('login/', LoginView.as_view(next_page='tasks_list'), name="login"),
    path('logout/', LogoutView.as_view(next_page='/'), name="logout"),
    path('dashboard/', views.TaskList.as_view(), name='tasks_list'),
    path('task-create', views.TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>', views.TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', views.DeleteView.as_view(), name='task-delete'),    
]