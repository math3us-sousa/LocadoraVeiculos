from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from sistema.views import Login, Home, Logout, Registro

urlpatterns = [
    path('', Login.as_view(), name='index'),
    path('home/', Home.as_view(), name='home'),
    path('logout/', Logout.as_view(), name='logout'),  
    path('registro/', Registro.as_view(), name='registro'),

    # Apenas as rotas de reset de senha — sem registrar 'login' nem 'logout' do Django
    path('senha/password_reset/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('senha/password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('senha/reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('senha/reset/done/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    path('admin/', admin.site.urls),
    path('veiculo/', include('veiculo.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
