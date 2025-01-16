"""
URL configuration for fbvcrudproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from testapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # Login and Logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Employee CRUD operations (with login required for protected views)
    path('', views.retrive_view, name='employee_list'),  # View all employees
    path('insert/', views.insert_view, name='employee_insert'),  # Insert new employee
    path('delete/<int:id>', views.delete_view, name='employee_delete'),  # Delete an employee
    path('update/<int:id>', views.update_view, name='employee_update'),  # Update employee data
    path('employee/<int:id>/', views.employee_detail, name='employee_detail'),  # Employee detail view
]
