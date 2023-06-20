"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from tasks.views import (
    delete_task,
    report_view,
    redirect_to_login,
    GenericTaskVew,
    GenericTaskCreateView,
    GenericTaskUpdateView,
    GenericTaskDeleteView,
    UserCreateView,
    UserLoginView,
    GenericTaskDetailView,
    GenericCompletedTasksView,
)


urlpatterns = [
    path("", redirect_to_login),
    path("admin/", admin.site.urls),
    path("signup", UserCreateView.as_view()),
    path("login", UserLoginView.as_view()),
    path("logout", LogoutView.as_view()),
    # Add all your views here
    path("tasks/", GenericTaskVew.as_view()),
    path("create_task", GenericTaskCreateView.as_view()),
    path("update_task/<pk>", GenericTaskUpdateView.as_view()),
    path("delete_task/<pk>", GenericTaskDeleteView.as_view()),
    path("delete-task/<int:task_id>/", delete_task),
    path("task/<pk>", GenericTaskDetailView.as_view()),
    path("completed_tasks/", GenericCompletedTasksView.as_view()),
    path("all_tasks/", report_view),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
