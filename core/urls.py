from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login padrão do Django
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # Logout
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # App gastos
    path('', include(('gastos.urls', 'gastos'), namespace='gastos')),
]
